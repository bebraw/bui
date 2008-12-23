# -*- coding: utf-8 -*-
from bui.utils.parser import read_yaml
from bui.utils.tree import TreeParent

from container import AbstractContainer

PRINT_BUTTON_EVENT_NAMES = True # put back to False at some point!

class BaseEventManager(object):
    def __init__(self, root_container, keys, events):
        assert isinstance(root_container, AbstractContainer)
        assert isinstance(keys, str)
        
        self.root_container = root_container
        self.events = events
        
        self.element_events = ElementEventContainer()
        self.key_events = EventContainer()
        self.state_events = EventContainer()
        
        self.construct_element_event_ids(self.root_container)
        self.construct_key_event_ids(keys)
        self.construct_state_event_ids(self.root_container)
    
    def construct_element_event_ids(self, elem):
        if isinstance(elem, TreeParent):
            for child in elem.children:
                event_handler = None
                
                if child.event_handler is not None and hasattr(self.events, child.event_handler):
                    event_handler = getattr(self.events, child.event_handler)
                else:
                    if child.name is not None:
                        handler_name = str(child.name).replace(' ', '_').lower()
                        
                        if hasattr(self.events, handler_name):
                            event_handler = getattr(self.events, handler_name)
                
                self.element_events.append(child, event_handler)
                
                self.construct_element_event_ids(child)
    
    def construct_key_event_ids(self, keys, key_mapping=None):
        def append_key_event(key, func_name, event):
            if hasattr(self.events, func_name):
                event_func = getattr(self.events, func_name)
                self.key_events.append(key, event_func, event)
        
        keys_structure = read_yaml(keys)
        
        if isinstance(keys_structure, dict):
            for key, value in keys_structure.items():
                if key_mapping and key_mapping.has_key(key):
                    key = key_mapping[key]
                elif len(key) == 1:
                    key = ord(key)
                
                if isinstance(value, dict):
                    for event, func_name in value.items():
                        append_key_event(key, func_name, event)
                else:
                    append_key_event(key, value, 'press')
    
    def construct_state_event_ids(self, elem):
        if isinstance(elem, TreeParent):
            for child in elem.children:
                if type(child.events) == dict:
                    for event, func_name in child.events.items():
                        event_handler = None
                        
                        if hasattr(self.events, func_name):
                            event_handler = getattr(self.events, func_name)
                        
                        self.state_events.append(child, event_handler, event)
                
                self.construct_state_event_ids(child)
    
    def element_event(self, evt):
        if self.element_events.has_key(evt):
            elem = self.element_events[evt].element
            func = self.element_events[evt].handler
            
            if PRINT_BUTTON_EVENT_NAMES:
                print func.__name__
            
            func(elem)
    
    def key_event(self, evt, pressed):
        if self.key_events.has_key(evt):
            key_event = self.key_events[evt]
            
            if pressed and key_event.press:
                key_event.press(self.root_container)
            elif hasattr(key_event, 'release'):
                key_event.release(self.root_container)
    
    def check_state_events(self, coordinate):
        triggered_event = False
        
        for element, state_event in self.state_events.items():
            if hasattr(state_event, 'on_mouse_over'):
                if coordinate.inside(element):
                    triggered_event = True
                    func = getattr(state_event, 'on_mouse_over')
                    func(self.root_container)
        
        return triggered_event

class EventContainer(dict):
    def append(self, element, handler, event):
        if handler:
            if not self.has_key(element):
                self[element] = Event()
            
            setattr(self[element], event, handler)

class Event():
    pass

# TODO: combine with EventContainer (allows to get rid of max_event_id)?
# in default case event could be press (merge with state events?)
class ElementEventContainer(EventContainer):
    def __init__(self):
        super(ElementEventContainer, self).__init__()
        self.max_event_id = 1
    
    def append(self, element, handler, event=None):
        if handler:
            for element_event in self.values():
                if element_event.element is element and element_event.handler is handler:
                    return
            
            element.event = self.max_event_id
            self[self.max_event_id] = ElementEvent(element, handler)
            self.max_event_id += 1

class ElementEvent(object):
    def __init__(self, element, handler):
        self.element = element
        self.handler = handler
