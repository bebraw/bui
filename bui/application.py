# -*- coding: utf-8 -*-
from constraint import BaseConstraintManager
from event import BaseEventManager
from layout import BaseLayoutManager
from serializer import unserialize
from window import BaseWindowManager

class BaseApplication(object):
    def __init__(self, structure, keys, events=None, constraints=None,
                 ui_initializer=None, element_height=20):
        self.root_container = unserialize(structure)
        
        self.constraint_manager = BaseConstraintManager(self.root_container, constraints)
        self.event_manager = BaseEventManager(self.root_container, keys, events)
        self.layout_manager = BaseLayoutManager(self.root_container, element_height)
        self.window_manager = BaseWindowManager()
        
        self.ui_initializer = ui_initializer
        if hasattr(ui_initializer, '__call__'):
            self.ui_initializer = ui_initializer
    
    def run(self):
        if self.ui_initializer:
            self.ui_initializer(self.root_container)
        # it would be nice to init layout just once and then alter on demand (ie. add/remove elements)
        # this needs to be detected somehow though
        #coord = self.window_manager.get_initial_coordinates()
        #self.layout_manager.initialize_layout()
    
    def gui(self):
        coord = self.window_manager.get_initial_coordinates()
        self.layout_manager.initialize_layout(coord) # not the most efficient solution but works
        self.constraint_manager.check_constraints()
        self.root_container.render()
