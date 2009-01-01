# -*- coding: utf-8 -*-
from Blender import Draw
from abstract import AbstractBlenderElement

class ColorPicker(AbstractBlenderElement):
    def initialize(self, **kvargs):
        self.value = (0.0, 0.0, 0.0, )
        super(ColorPicker, self).initialize(**kvargs)
    
    def render(self):
        Draw.ColorPicker(self.event, self.x, self.y,
                         self.width, self.height, self.value,
                         self.tooltip, self.update_value)
