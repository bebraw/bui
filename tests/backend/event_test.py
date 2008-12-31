# -*- coding: utf-8 -*-
import bui.backend.event

from bui.backend.container import *
from bui.backend.event import BaseEventManager
from bui.backend.serializer import unserialize

from bui.utils.coordinate import Coordinate
from bui.utils.meta import AllMethodsStatic

from ..structure import MinimalStructure, StructureForEventTests, \
                      StructureForStateEventTests, structure_keys

bui.backend.event.PRINT_BUTTON_EVENT_NAMES = True

PRESS = 1
RELEASE = 0

class Events(AllMethodsStatic):
    def add_monkey(elem):
        pass
    
    def delete_all(elem):
        pass
    
    def press_s(elem):
        pass
    
    def release_s(elem):
        pass
    
    def add_to_ui_structure(elem):
        root_elem = elem.find_root_element()
        structure_root = unserialize(MinimalStructure())
        root_elem.append(structure_root)

class TestBaseEventManager():
    def setup_method(self, method):
        self.root_container = unserialize(StructureForEventTests)
        self.add_monkey_elem = self.root_container.children[0]
        self.delete_all_elem = self.root_container.children[2]
        self.add_to_ui_structure = self.root_container.children[3]
        
        self.event_manager = BaseEventManager(self.root_container, structure_keys, Events)
    
    def test_manager_has_right_element_events(self):
        assert self.event_manager.element_events[1].element == self.add_monkey_elem
        assert self.event_manager.element_events[1].handler == Events.add_monkey
        
        assert self.event_manager.element_events[2].element == self.delete_all_elem
        assert self.event_manager.element_events[2].handler == Events.delete_all
        
        assert self.event_manager.element_events[3].element == self.add_to_ui_structure
        assert self.event_manager.element_events[3].handler == Events.add_to_ui_structure
        
        assert len(self.event_manager.element_events) == 3
        assert self.event_manager.element_events.max_event_id == 4
    
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
        
        # should be 200 as root container width constraints this
        # where and when to check this??? TODO: handle with properties!
        assert self.root_container.children[4].width == 400
    
    def test_manager_has_right_key_events(self):
        assert self.event_manager.key_events[ord('a')].press == Events.add_monkey
        assert self.event_manager.key_events[ord('d')].press == Events.delete_all
        assert self.event_manager.key_events[ord('s')].press == Events.press_s
        assert self.event_manager.key_events[ord('s')].release == Events.release_s
    
    def test_trigger_key_events(self):
        self.event_manager.key_event('a', PRESS)
        self.event_manager.key_event('d', PRESS)
        self.event_manager.key_event('s', PRESS)
        self.event_manager.key_event('s', RELEASE)

class StateEvents():
    @staticmethod
    def print_foo(elem):
        print 'foo'

class TestStateEvents():
    def setup_method(self, method):
        self.root_container = unserialize(StructureForStateEventTests)
        self.print_foo_elem = self.root_container.children[0]
        self.event_manager = BaseEventManager(self.root_container, structure_keys, StateEvents)
    
    def test_manager_has_right_element_events(self):
        assert len(self.event_manager.element_events) == 0
        assert len(self.event_manager.state_events) == 1
        assert self.event_manager.state_events[self.print_foo_elem].on_mouse_over == StateEvents.print_foo
    
    def test_trigger_state_events(self):
        self.event_manager.check_state_events(Coordinate(10, 10)) # should print foo
        self.event_manager.check_state_events(Coordinate(700, 10)) # should NOT print foo
    
    def test_element_is_removed(self):
        pass # should make it sure event gets removed too! (add to upper test class too!)
