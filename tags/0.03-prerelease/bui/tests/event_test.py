# -*- coding: utf-8 -*-
import bui.event

from bui.container import *
from bui.event import EventManager
from bui.serializer import unserialize

from structure import MinimalStructure, StructureForEventTests, structure_keys

bui.event.PRINT_BUTTON_EVENT_NAMES = True

PRESS = 1
RELEASE = 0

class Events():
    @staticmethod
    def add_monkey(elem):
        pass
    
    @staticmethod
    def delete_all(elem):
        pass
    
    @staticmethod
    def press_s(elem):
        pass
    
    @staticmethod
    def release_s(elem):
        pass
    
    @staticmethod
    def add_to_ui_structure(elem):
        root_elem = elem.find_root_element()
        structure_root = unserialize(MinimalStructure())
        root_elem.add_child_structure(structure_root)

class TestEventManager():
    def setup_method(self, method):
        self.root_container = unserialize(StructureForEventTests())
        self.add_monkey_elem = self.root_container.children[0]
        self.delete_all_elem = self.root_container.children[2]
        self.add_to_ui_structure = self.root_container.children[3]
        
        self.event_manager = EventManager(self.root_container, structure_keys, Events, 20)
    
    def test_manager_has_right_element_events(self):
        assert self.event_manager.element_events[1].element == self.add_monkey_elem
        assert self.event_manager.element_events[1].handler == Events.add_monkey
        
        assert self.event_manager.element_events[2].element == self.delete_all_elem
        assert self.event_manager.element_events[2].handler == Events.delete_all
        
        assert self.event_manager.element_events[3].element == self.add_to_ui_structure
        assert self.event_manager.element_events[3].handler == Events.add_to_ui_structure
        
        assert len(self.event_manager.element_events) == 3
        assert self.event_manager.max_event_id == 4
    
    def test_construct_element_event_ids(self):
        # note that event ids have already been constructed once in __init__!
        self.event_manager.construct_element_event_ids(self.root_container)
        self.test_manager_has_right_element_events()
    
    def test_trigger_element_events(self):
        self.event_manager.element_event(1)
        self.event_manager.element_event(2)
    
    def test_add_to_ui_structure(self):
        assert len(self.root_container.children) == 4
        
        self.event_manager.element_event(3) # adds new VerticalContainer to the structure!
        
        assert len(self.root_container.children) == 5
        assert self.root_container.children[4].width == 200 # root container width restricts this!
    
    def test_manager_has_right_key_events(self):
        assert self.event_manager.key_events['a'].press == Events.add_monkey
        assert self.event_manager.key_events['d'].press == Events.delete_all
        assert self.event_manager.key_events['s'].press == Events.press_s
        assert self.event_manager.key_events['s'].release == Events.release_s
    
    def test_trigger_key_events(self):
        self.event_manager.key_event('a', PRESS)
        self.event_manager.key_event('d', PRESS)
        self.event_manager.key_event('s', PRESS)
        self.event_manager.key_event('s', RELEASE)
