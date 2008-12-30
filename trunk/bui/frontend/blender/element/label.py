# -*- coding: utf-8 -*-
from Blender import Draw

from abstract import AbstractBlenderElement

class Label(AbstractBlenderElement):
    def render(self):
        Draw.Label(self.name, self.x, self.y, self.width, self.height)
