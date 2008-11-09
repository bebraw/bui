# -*- coding: utf-8 -*-
import bui.event

from bui.container import VerticalContainer
from bui.element import EmptyElement
from bui.event import EventManager
from bui.serializer import serialize

from structure import minimal_structure, structure_for_event_tests, structure_keys

bui.event.PRINT_BUTTON_EVENT_NAMES = True

def add_monkey(elem):
    pass # could assert elem here!

def delete_all(elem):
    pass # could assert elem here!

def add_to_ui_structure(elem):
    # could assert elem here!
    root_elem = elem.find_root_element()
    structure_root = serialize(minimal_structure, globals())
    root_elem.add_child_structure(structure_root)
    return structure_root

class TestEventManager():
    def setup_method(self, method):
        self.root_container = serialize(structure_for_event_tests, globals())
        self.add_monkey_elem = self.root_container.children[0]
        self.delete_all_elem = self.root_container.children[2]
        self.add_to_ui_structure = self.root_container.children[3]
        
        self.event_manager = EventManager(self.root_container, structure_keys, globals(), 20)
    
    def test_manager_has_right_element_events(self):
        assert self.event_manager.element_events[1].element == self.add_monkey_elem
        assert self.event_manager.element_events[1].handler == add_monkey
        
        assert self.event_manager.element_events[2].element == self.delete_all_elem
        assert self.event_manager.element_events[2].handler == delete_all
        
        assert self.event_manager.element_events[3].element == self.add_to_ui_structure
        assert self.event_manager.element_events[3].handler == add_to_ui_structure
        
        assert len(self.event_manager.element_events) == 3
        assert self.event_manager.max_event_id == 4
    
    def test_trigger_element_events(self):
        self.event_manager.element_event(1)
        self.event_manager.element_event(2)
    
    def test_add_to_ui_structure(self):
        self.event_manager.element_event(3)
        
        assert self.root_container.children[4].width == 400
    
    def test_manager_has_right_key_events(self):
        assert self.event_manager.key_events['a'] == add_monkey
        assert self.event_manager.key_events['d'] == delete_all
    
    def test_trigger_key_events(self):
        self.event_manager.key_event('a', 1)
        self.event_manager.key_event('d', 1)
