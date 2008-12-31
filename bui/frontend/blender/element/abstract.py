# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject
from bui.graphics.opengl.draw import draw_rectangle

# TODO: this is common for all opengl implementations -> to util funcs
# NOTE: this needs to be set directly to AbstractObject so that it affects containers too!
def render_bg_color(self):
    if self.bg_color:
        draw_rectangle(self.bg_color, self.x, self.y, self.x + self.width, self.y + self.height)

setattr(AbstractObject, 'render_bg_color', render_bg_color)

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
