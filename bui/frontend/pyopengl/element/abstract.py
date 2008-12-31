# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject

from bui.graphics.opengl.draw import draw_rectangle

# TODO: this is common for all opengl implementations -> to util funcs
# NOTE: this needs to be set directly to AbstractObject so that it affects containers too!
def render_bg_color(self):
    if self.bg_color:
        draw_rectangle(self.bg_color, self.x, self.y, self.x + self.width, self.y + self.height)

setattr(AbstractObject, 'render_bg_color', render_bg_color)

class AbstractOpenGLElement(AbstractObject):
    def initialize(self, **kvargs):
        self.tooltip = ''
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        super(AbstractOpenGLElement, self).initialize(**kvargs)
