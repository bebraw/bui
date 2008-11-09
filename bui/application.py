# -*- coding: utf-8 -*-
from constraint import ConstraintManager
from event import EventManager
from serializer import serialize
from window import WindowManager

class Application(object):
    def __init__(self, structure, keys, namespace, element_height=20):
        self.root_container = serialize(structure, namespace)
        self.root_container.initialize_element_heights(element_height)
        self.root_container.initialize_element_widths(self.root_container.width)
        
        self.constraint_manager = ConstraintManager(self.root_container, namespace)
        self.event_manager = EventManager(self.root_container, keys, namespace, element_height)
        self.window_manager = WindowManager()
    
    def run(self):
        pass
    
    def _gui(self):
        self.constraint_manager.check_constraints()
        self.window_manager.__init__()
        self.root_container.render(self.window_manager)
