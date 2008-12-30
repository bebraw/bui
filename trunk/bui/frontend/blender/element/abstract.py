# -*- coding: utf-8 -*-
import Blender

from bui.backend.abstract import AbstractChild, AbstractObject

# right place for binding? (should probably use separate func for this) see separator.py too!
import bui.graphics.opengl.draw
setattr(bui.graphics.opengl.draw, 'ogl', Blender.BGL)

from bui.graphics.opengl.draw import draw_rectangle

# NOTE: this needs to be set directly to AbstractObject so that it affects containers too!
def render_bg_color(self):
    if self.bg_color:
        draw_rectangle(self.bg_color, self.x, self.y, self.x + self.width, self.y + self.height)

setattr(AbstractObject, 'render_bg_color', render_bg_color)

class AbstractBlenderElement(AbstractChild):
    def __init__(self):
        super(AbstractBlenderElement, self).__init__()
        self.event = 0
    
    def initialize(self, **kvargs):
        self.tooltip = ''
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        super(AbstractBlenderElement, self).initialize(**kvargs)
    
    def update_value(self, evt, val):
        self.value = val
    
    def render(self):
        super(AbstractBlenderElement, self).render()
        #print self.x, self.y, self.common.window_manager.height
