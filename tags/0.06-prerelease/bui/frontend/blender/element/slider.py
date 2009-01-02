# -*- coding: utf-8 -*-
from Blender import Draw
from abstract import AbstractBlenderElement

class Slider(AbstractBlenderElement):
    def initialize(self, **kvargs):
        self.label = ''
        
        self.value = 0.0
        self.min = 0.0
        self.max = 1.0
        
        super(Slider, self).initialize(**kvargs)
    
    def render(self):
        Draw.Slider(self.label + ': ', self.event, self.x, self.y,
                    self.width, self.height, self.value, self.min, self.max,
                    False, self.tooltip, self.update_value)
