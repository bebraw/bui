# -*- coding: utf-8 -*-
import os

try:
    import Blender
    from Blender import BGL, Draw
except ImportError:
    pass

from bui.abstract import AbstractElement

# TODO: move to utils at some point!
def find_file_path(root_dir, file_name):
    """ Returns path to given file_name with file_name appended. """
    for root, dirs, files in os.walk(root_dir):
        if file_name in files:
            return os.path.join(root, file_name)

class AbstractBlenderElement(AbstractElement):
    def __init__(self, **kvargs):
        self.event = 0
        self.tooltip = ''
        self.value = 0
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        super(AbstractBlenderElement, self).__init__(**kvargs)
    
    def update_value(self, evt, val):
        self.value = val

class Label(AbstractBlenderElement):
    def render(self, coord):
        self.label = Draw.Label(self.name, coord.x, coord.y - self.height, self.width, self.height)

class TextBox(AbstractBlenderElement):
    def render(self, coord):
        self.textbox = Draw.String(self.name + ': ', self.event, coord.x, coord.y - self.height, self.width, self.height,
                              self.value, self.max_input_length, self.tooltip, self.update_value)

class ToggleButton(AbstractBlenderElement):
    def render(self, coord):
        self.togglebutton = Draw.Toggle(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                                   self.value, self.tooltip, self.update_value)

class PushButton(AbstractBlenderElement):
    def render(self, coord):
        self.pushbutton = Draw.PushButton(self.name, self.event, coord.x, coord.y - self.height, self.width,
                                          self.height, self.tooltip)

class Menu(AbstractBlenderElement):
    def render(self, coord):
        self.menu = Draw.Menu(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                         self.value, self.tooltip, self.update_value)

class Slider(AbstractBlenderElement):
    def render(self, coord):
        self.slider = Draw.Slider(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                                  self.value, self.min, self.max, False, self.tooltip, self.update_value)

class Number(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.range = 0 # no clickstep
        self.precision = 0.0 # 4 decimals
        super(Number, self).__init__(**kvargs)
        self.value = float(self.value)
    
    def render(self, coord):
        try:
            self.number = Draw.Number(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                                  self.value, self.min, self.max, self.tooltip, self.update_value, self.range, self.precision)
        except: # needed for backwards compatibility (no range and precision in 2.48a)
            self.number = Draw.Number(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                                  self.value, self.min, self.max, self.tooltip, self.update_value)

class IntNumber(AbstractBlenderElement):
    def render(self, coord):
        self.number = Draw.Number(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                                  int(self.value), int(self.min), int(self.max), self.tooltip, self.update_value)

class Image(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.image = ''
        self.x_zoom = 1.0
        self.y_zoom = 1.0
        self.x_clip = 0
        self.y_clip = 0
        self.clip_width = -1
        self.clip_height = -1
        self.image_block = None
        super(Image, self).__init__(**kvargs)
        
        uscriptsdir = Blender.Get('uscriptsdir')
        file_path = find_file_path(uscriptsdir, self.image)
        
        if file_path:
            self.image_block = Blender.Image.Load(file_path)
            width, height = self.image_block.getSize()
            
            if not self.height:
                self.height = height
            
            if not self.width:
                self.width = width
    
    def render(self, coord):
        if self.image_block:
            BGL.glEnable(BGL.GL_BLEND)
            BGL.glBlendFunc(BGL.GL_SRC_ALPHA, BGL.GL_ONE_MINUS_SRC_ALPHA) 
            
            Draw.Image(self.image_block, coord.x, coord.y - self.height,
                       self.x_zoom, self.y_zoom, self.x_clip, self.y_clip,
                       self.clip_width, self.clip_height)
            
            BGL.glDisable(BGL.GL_BLEND)
