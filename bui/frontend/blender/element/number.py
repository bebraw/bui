# -*- coding: utf-8 -*-
from Blender import Draw
from abstract import AbstractBlenderElement

class Number(AbstractBlenderElement):
    def initialize(self, **kvargs):
        self.range = 0 # no clickstep
        self.precision = 0.0 # 4 decimals
        self.value = 0.0
        super(Number, self).initialize(**kvargs)
        self.value = float(self.value)
    
    def render(self):
        try:
            Draw.Number(self.name, self.event, self.x, self.y,
                        self.width, self.height, self.value, self.min, self.max,
                        self.tooltip, self.update_value, self.range, self.precision)
        except: # needed for backwards compatibility (no range and precision in 2.48a)
            Draw.Number(self.name, self.event, self.x, self.y,
                        self.width, self.height, self.value, self.min, self.max,
                        self.tooltip, self.update_value)

class IntNumber(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0
        super(IntNumber, self).__init__(**kvargs)
    
    def render(self):
        Draw.Number(self.name, self.event, self.x, self.y,
                    self.width, self.height, int(self.value), int(self.min),
                    int(self.max), self.tooltip, self.update_value)
