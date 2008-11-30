# -*- coding: utf-8 -*-
import bui.event

from bui.container import *
from bui.event import BaseEventManager
from bui.serializer import unserialize

from structure import MinimalStructure, StructureForEventTests, \
                      StructureForStateEventTests, structure_keys

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

class TestBaseEventManager():
    def setup_method(self, method):
        self.root_container = unserialize(StructureForEventTests)
        self.add_monkey_elem = self.root_container.children[0]
        self.delete_all_elem = self.root_container.children[2]
        self.add_to_ui_structure = self.root_container.children[3]
        
        self.event_manager = BaseEventManager(self.root_container, structure_keys, Events, 20)
    
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

class StateEvents():
    @staticmethod
    def print_foo(elem):
        print 'foo'

# TODO: move to coordinate.py!
class Coordinate():
    def __init__(self, x, y):
        assert type(x) == int
        assert type(y) == int
        self.x = x
        self.y = y
    
    def inside(self, element):
        #print element.x, element.y # TODO: note some object needs to set these? (check initializer funcs)
        return True

class TestStateEvents():
    def setup_method(self, method):
        self.root_container = unserialize(StructureForStateEventTests)
        self.print_foo_elem = self.root_container.children[0]
        
        # figure out how to attach state event to element (weak reference in case element is removed?)
        # on redraw event manager should check state events and trigger those that match
        
        self.event_manager = BaseEventManager(self.root_container, structure_keys, StateEvents, 20)
    
    def test_manager_has_right_element_events(self):
        assert len(self.event_manager.element_events) == 0
        assert len(self.event_manager.state_events) == 1
        assert self.event_manager.state_events[self.print_foo_elem].on_mouse_over == StateEvents.print_foo
    
    def test_trigger_state_events(self):
        self.event_manager.check_state_events(Coordinate(10, 10)) # should print foo
        self.event_manager.check_state_events(Coordinate(700, 10)) # FIXME: should NOT print foo
    
    def test_element_is_removed(self):
        pass # should make it sure event gets removed too! (add to upper test class too!)
