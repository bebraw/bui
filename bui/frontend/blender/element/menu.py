# -*- coding: utf-8 -*-
from Blender import Draw

from abstract import AbstractBlenderElement

# TODO: add rest of menus (Popup etc.). Also rethink the mapping between definition
# and the element.

class Menu(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0
        super(Menu, self).__init__(**kvargs)
    
    def render(self):
        Draw.Menu(self.name, self.event, self.x, self.y,
                  self.width, self.height, self.value, self.tooltip,
                  self.update_value)
