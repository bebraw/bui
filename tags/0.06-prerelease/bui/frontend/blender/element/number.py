# -*- coding: utf-8 -*-
from Blender import Draw
from abstract import AbstractBlenderElement

class Number(AbstractBlenderElement):
    def initialize(self, **kvargs):
        self.label = ''
        
        self.value = 0.0
        self.min = 0.0
        self.max = 1.0
        
        self.range = 0 # no clickstep
        self.precision = 0.0 # 4 decimals
        
        super(Number, self).initialize(**kvargs)
        self.value = float(self.value)
    
    def render(self):
        try:
            Draw.Number(self.label, self.event, self.x, self.y,
                        self.width, self.height, self.value, self.min, self.max,
                        self.tooltip, self.update_value, self.range, self.precision)
        except: # needed for backwards compatibility (no range and precision in 2.48a)
            Draw.Number(self.label, self.event, self.x, self.y,
                        self.width, self.height, self.value, self.min, self.max,
                        self.tooltip, self.update_value)

class IntNumber(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.label = ''
        
        self.value = 0
        self.min = 0
        self.max = 1
        
        super(IntNumber, self).__init__(**kvargs)
    
    def render(self):
        Draw.Number(self.label, self.event, self.x, self.y,
                    self.width, self.height, self.value, self.min,
                    self.max, self.tooltip, self.update_value)
