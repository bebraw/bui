# -*- coding: utf-8 -*-
from Blender import Draw
from abstract import AbstractBlenderElement

class Label(AbstractBlenderElement):
    def initialize(self, **kvargs):
        self.label = ''
        super(Label, self).initialize(**kvargs)
    
    def render(self):
        Draw.Label(self.label, self.x, self.y, self.width, self.height)
