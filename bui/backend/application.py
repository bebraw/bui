# -*- coding: utf-8 -*-
from bui.backend.serializer import unserialize

from constraint import BaseConstraintManager
from event import BaseEventManager
from window import BaseWindowManager

class BaseApplication(object):
    def __init__(self, structure, keys, events=None, constraints=None,
                 ui_initializer=None, element_height=20):
        self.root_layout = unserialize(structure)
        self.root_layout.common.element_height = 20
        self.root_layout.common.application = self
        
        self.constraint_manager = BaseConstraintManager(self.root_layout, constraints)
        self.event_manager = BaseEventManager(self.root_layout, keys, events)
        self.window_manager = BaseWindowManager()
        
        self.ui_initializer = ui_initializer
        if hasattr(ui_initializer, '__call__'):
            self.ui_initializer = ui_initializer
    
    def redraw(self):
        # TODO: trigger constraint check only by events???
        # TODO: get rid of this?
        self.constraint_manager.check_constraints()
        
        self.root_layout.render(render_coordinate=None) # override with begin_render???
    
    def run(self):
        if self.ui_initializer:
            self.ui_initializer(self.root_layout)
    
    # TODO: get rid of this?
    def update_structure(self):
        # nasty hack as the updates are not nice yet (gets called during unserialize)
        if hasattr(self, 'event_manager'):
            self.event_manager.construct_element_event_ids(self.root_layout)
