# -*- coding: utf-8 -*-
import OpenGL.GL

from bui.backend.abstract import AbstractChild, AbstractObject

# set drawing functions to use Blender's OpenGL implementation
# TODO: tidy up (get rid of ogl and just dump whole namespace into draw?)
import bui.graphics.opengl.draw
setattr(bui.graphics.opengl.draw, 'ogl', OpenGL.GL)

from bui.graphics.opengl.draw import draw_rectangle

# TODO: this is common for all opengl implementations -> to util funcs
# NOTE: this needs to be set directly to AbstractObject so that it affects containers too!
def render_bg_color(self):
    print self.bg_color, self.x, self.y, self.width, self.height
    if self.bg_color:
        draw_rectangle(self.bg_color, self.x, self.y, self.x + self.width, self.y + self.height)

setattr(AbstractObject, 'render_bg_color', render_bg_color)

class AbstractOpenGLElement(AbstractChild):
    def __init__(self):
        super(AbstractOpenGLElement, self).__init__()
        self.event = 0
    
    def initialize(self, **kvargs):
        self.tooltip = ''
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        super(AbstractOpenGLElement, self).initialize(**kvargs)
    
    def update_value(self, evt, val):
        self.value = val
