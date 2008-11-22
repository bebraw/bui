# -*- coding: utf-8 -*-
from constraint import ConstraintManager
from event import EventManager
from initializer import initialize_element_heights, initialize_element_widths
from serializer import unserialize
from window import WindowManager

class Application(object):
    def __init__(self, structure, keys, events=None, constraints=None, element_height=20):
        self.root_container = unserialize(structure)
        initialize_element_heights(self.root_container, element_height)
        initialize_element_widths(self.root_container)
        
        self.constraint_manager = ConstraintManager(self.root_container, constraints)
        self.event_manager = EventManager(self.root_container, keys, events, element_height)
        self.window_manager = WindowManager()
    
    def run(self):
        pass
    
    def _gui(self):
        self.constraint_manager.check_constraints()
        self.event_manager.construct_element_event_ids(self.root_container)
        self.window_manager.__init__()
        self.root_container.render(self.window_manager)
