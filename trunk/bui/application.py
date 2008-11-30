# -*- coding: utf-8 -*-
from constraint import BaseConstraintManager
from event import BaseEventManager
from initializer import initialize_element_heights, initialize_element_widths
from serializer import unserialize
from window import BaseWindowManager

class BaseApplication(object):
    def __init__(self, structure, keys, events=None, constraints=None, element_height=20):
        self.root_container = unserialize(structure)
        
        initialize_element_heights(self.root_container, element_height)
        initialize_element_widths(self.root_container)
        
        self.constraint_manager = BaseConstraintManager(self.root_container, constraints)
        self.event_manager = BaseEventManager(self.root_container, keys, events, element_height)
        self.window_manager = BaseWindowManager()
    
    def run(self):
        pass
    
    def gui(self):
        self.constraint_manager.check_constraints()
        self.event_manager.construct_element_event_ids(self.root_container) # TODO: in right place?
        self.window_manager.__init__() # TODO: needed even? (if coords go to objects, this can be removed...)
        self.root_container.render(self.window_manager)
