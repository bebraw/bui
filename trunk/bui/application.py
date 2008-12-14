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
        self.root_container.application = self
        
        self.constraint_manager = BaseConstraintManager(self.root_container, constraints)
        self.event_manager = BaseEventManager(self.root_container, keys, events)
        self.window_manager = BaseWindowManager()
        self.layout_manager = BaseLayoutManager(self.window_manager, self.root_container, element_height)
        
        self.ui_initializer = ui_initializer
        if hasattr(ui_initializer, '__call__'):
            self.ui_initializer = ui_initializer
    
    def gui(self):
        # TODO: trigger constraint check only by events???
        self.constraint_manager.check_constraints()
        self.layout_manager.initialize_layout() # checking constraints may alter layout
        self.root_container.render()
    
    def run(self):
        if self.ui_initializer:
            self.ui_initializer(self.root_container)
    
    def update_structure(self):
        self.event_manager.construct_element_event_ids(self.root_container)
