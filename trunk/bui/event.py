# -*- coding: utf-8 -*-
from bui.container import AbstractContainer
from bui.parser import read_yaml
from bui.tree import TreeParent

PRINT_BUTTON_EVENT_NAMES = True # put back to False at some point!

class ElementEvent(object):
    def __init__(self, element, handler):
        self.element = element
        self.handler = handler

class EventManager(object):
    def __init__(self, root_container, keys, namespace, element_height):
        assert isinstance(root_container, AbstractContainer)
        assert isinstance(keys, str)
        assert isinstance(namespace, dict)
        assert isinstance(element_height, int)
        
        self.root_container = root_container
        self.namespace = namespace
        self.element_height = element_height
        
        self.element_events = {}
        self.key_events = {}
        
        self.max_event_id = 1
        
        self.construct_element_event_ids(self.root_container)
        self._construct_key_event_ids(keys)
    
    def construct_element_event_ids(self, elem):
        if isinstance(elem, TreeParent):
            for child in elem.children:
                event_handler = None
                
                if hasattr(child, 'event_handler'):
                    event_handler = self.namespace[child.event_handler]
                else:
                    if hasattr(child, 'name'):
                        handler_name = str(child.name).replace(' ', '_').lower() #+ '_event'
                        
                        if self.namespace.has_key(handler_name):
                            event_handler = self.namespace[handler_name]
                
                if event_handler:
                    self._add_element_event(child, event_handler)
                
                self.construct_element_event_ids(child)
    
    def _add_element_event(self, elem, handler):
        for element_event in self.element_events.values():
            if element_event.element is elem and element_event.handler is handler:
                return
        
        elem.event = self.max_event_id
        self.element_events[self.max_event_id] = ElementEvent(elem, handler)
        self.max_event_id += 1
    
    def _construct_key_event_ids(self, keys):
        keys_structure = read_yaml(keys)
        
        if isinstance(keys_structure, dict):
            for key, func_name in keys_structure.items():
                if self.namespace.has_key(func_name):
                    self.key_events[key] = self.namespace[func_name]
    
    def element_event(self, evt):
        if self.element_events.has_key(evt):
            elem = self.element_events[evt].element
            func = self.element_events[evt].handler
            
            if PRINT_BUTTON_EVENT_NAMES:
                print func.__name__
            
            func(elem)
    
    def key_event(self, evt, val):
        if self.key_events.has_key(evt):
            self.key_events[evt](self.root_container)
