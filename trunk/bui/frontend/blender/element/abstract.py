# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject

class AbstractBlenderElement(AbstractObject):
    def initialize(self, **kvargs):
        self.event = 0
        self.tooltip = ''
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        super(AbstractBlenderElement, self).initialize(**kvargs)
    
    def update_value(self, evt, val):
        self.value = val
    
    def render(self):
        super(AbstractBlenderElement, self).render()
