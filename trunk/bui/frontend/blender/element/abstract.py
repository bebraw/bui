# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject
from bui.backend.element.abstract import AbstractElement

# NOTE: this needs to be set directly to AbstractObject so that it affects containers too!
def render_bg_color(self):
    if self.bg_color:
        draw_rectangle(self.bg_color, self.x, self.y, self.x + self.width, self.y + self.height)

setattr(AbstractObject, 'render_bg_color', render_bg_color)

class AbstractBlenderElement(AbstractElement):
    def __init__(self, **kvargs):
        self.event = 0
        self.tooltip = ''
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        super(AbstractBlenderElement, self).__init__(**kvargs)
    
    def update_value(self, evt, val):
        self.value = val
