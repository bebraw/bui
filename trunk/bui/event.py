# -*- coding: utf-8 -*-
from bui.container import AbstractContainer

'''
TODO:
-handle event seeking
-PRINT_BUTTON_EVENT_NAMES should be False here and redefined upper if wanted!
-write iterator for ui tree children (makes it easier to use construct_button_event_ids) + cleans up code
-enhance key event handling!
'''

PRINT_BUTTON_EVENT_NAMES = True

class ElementEvent(object):
    def __init__(self, element, handler):
        self.element = element
        self.handler = handler

class EventManager(object):
    def __init__(self, root_container, namespace, element_height):
        assert isinstance(root_container, AbstractContainer)
        
        self.element_height = element_height
        
        self.element_events = {}
        self.key_events = {}
        
        self.max_event_id = 1
        
        self._construct_element_event_ids(root_container, namespace)
        # self._construct_key_event_ids(event_list, namespace) # needs event_list via __init__ ! reuse above func for this
    
    def _construct_element_event_ids(self, element, namespace):
        if element.children:
            for child in element.children:
                event_handler = None
                
                if child.event_handler:
                    event_handler = namespace[child.event_handler]
                else:
                    handler_name = str(child.name).replace(' ', '_').lower() #+ '_event'
                    
                    if globals().has_key(handler_name):
                        event_handler = namespace[handler_name]
                
                if event_handler:
                    self._add_element_event(child, event_handler)
                
                self._construct_element_event_ids(child, namespace)
    
    def _add_element_event(self, elem, handler):
        elem.event = self.max_event_id
        self.element_events[self.max_event_id] = ElementEvent(elem, handler)
        self.max_event_id += 1
    
    def element_event(self, evt):
        if self.element_events.has_key(evt):
            elem = self.element_events[evt].element
            func = self.element_events[evt].handler
            
            if PRINT_BUTTON_EVENT_NAMES:
                print func.__name__
            
            new_elem_root = func(elem)
            
            if new_elem_root:
                self.construct_button_event_ids(new_elem_root)
                new_elem_root.initialize_element_heights(self.element_height)
                new_elem_root.initialize_element_widths(new_elem_root.parent.width)
    
    def key_event(self, evt, val):
        if self.key_events.has_key(evt):
            self.key_events[evt]()
