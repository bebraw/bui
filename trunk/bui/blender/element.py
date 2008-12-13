# -*- coding: utf-8 -*-
import os

try:
    import Blender
    from Blender import Draw
except ImportError:
    pass

from bui.abstract import AbstractElement
from bui.container import HorizontalContainer, VerticalContainer

from icons import BLENDER_ICONS
from utils import *

class AbstractBlenderElement(AbstractElement):
    def __init__(self, **kvargs):
        self.event = 0
        self.tooltip = ''
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        super(AbstractBlenderElement, self).__init__(**kvargs)
    
    def render_bg_color(self):
        if self.bg_color:
            BGL.glColor3f(*self.bg_color)
            BGL.glRectf(self.x, self.y, self.x + self.width, self.y + self.height)
    
    def update_value(self, evt, val):
        self.value = val

class Separator(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.color = 3*[0.0]
        super(Separator, self).__init__(**kvargs)
    
    def render(self):
        text_sep_dist = 10
        
        if isinstance(self.parent, HorizontalContainer):
            x_coord = self.x + self.width / 2.0
            
            # TODO: implement name rendering (should rotate Draw.Text somehow?)
            draw_line(0.5, self.color, x_coord, self.y, x_coord, self.y + self.height)
        
        if isinstance(self.parent, VerticalContainer):
            y_coord = self.y + self.height / 2.0
            
            # HACK! draw text in some not visible place to get its width (needed for centering)
            BGL.glRasterPos2f(-10000.0, -10000.0)
            text_width = Draw.Text(self.name)
            
            text_x = self.x + (self.width - text_width) / 2.0
            
            sep_begin_x = self.x
            sep_end_x = max(sep_begin_x, text_x - text_sep_dist)
            draw_line(0.5, self.color, sep_begin_x, y_coord, sep_end_x, y_coord)
            
            text_y_coord = y_coord - 5 # 10 = half of text height
            BGL.glRasterPos2f(text_x, text_y_coord)
            Draw.Text(self.name)
            
            sep_end_x = self.x + self.width
            sep_begin_x = min(sep_end_x, text_x + text_width + text_sep_dist)
            draw_line(0.5, self.color, sep_begin_x, y_coord, sep_end_x, y_coord)

class Label(AbstractBlenderElement):
    def render(self):
        Draw.Label(self.name, self.x, self.y, self.width, self.height)

class TextBox(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = ''
        super(TextBox, self).__init__(**kvargs)
    
    def render(self):
        Draw.String(self.name + ': ', self.event, self.x, self.y,
                    self.width, self.height, self.value, self.max_input_length,
                    self.tooltip, self.update_value)

class ToggleButton(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = False
        super(ToggleButton, self).__init__(**kvargs)
    
    def render(self):
        Draw.Toggle(self.name, self.event, self.x, self.y,
                    self.width, self.height, self.value, self.tooltip,
                    self.update_value)

class PushButton(AbstractBlenderElement):
    def render(self):
        Draw.PushButton(self.name, self.event, self.x, self.y,
                        self.width, self.height, self.tooltip)

class Menu(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0
        super(Menu, self).__init__(**kvargs)
    
    def render(self):
        Draw.Menu(self.name, self.event, self.x, self.y,
                  self.width, self.height, self.value, self.tooltip,
                  self.update_value)

class Slider(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0.0
        super(Slider, self).__init__(**kvargs)
    
    def render(self):
        Draw.Slider(self.name + ': ', self.event, self.x, self.y,
                    self.width, self.height, self.value, self.min, self.max,
                    False, self.tooltip, self.update_value)

class Number(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.range = 0 # no clickstep
        self.precision = 0.0 # 4 decimals
        self.value = 0.0
        super(Number, self).__init__(**kvargs)
        self.value = float(self.value)
    
    def render(self):
        try:
            Draw.Number(self.name, self.event, self.x, self.y,
                        self.width, self.height, self.value, self.min, self.max,
                        self.tooltip, self.update_value, self.range, self.precision)
        except: # needed for backwards compatibility (no range and precision in 2.48a)
            Draw.Number(self.name, self.event, self.x, self.y,
                        self.width, self.height, self.value, self.min, self.max,
                        self.tooltip, self.update_value)

class IntNumber(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0
        super(IntNumber, self).__init__(**kvargs)
    
    def render(self):
        Draw.Number(self.name, self.event, self.x, self.y,
                    self.width, self.height, int(self.value), int(self.min),
                    int(self.max), self.tooltip, self.update_value)

class ColorPicker(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = (0.0, 0.0, 0.0, )
        super(ColorPicker, self).__init__(**kvargs)
    
    def render(self):
        Draw.ColorPicker(self.event, self.x, self.y,
                         self.width, self.height, self.value,
                         self.tooltip, self.update_value)

'''
FIXME: self.update_value callback doesn't get called for some reason -> value does not get updated
class Normal(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = (1.0, 1.0, 1.0, )
        super(Normal, self).__init__(**kvargs)
    
    def render(self):
        Draw.Normal(self.event, self.x, self.y, self.width,
                    self.height, self.value, self.tooltip, self.update_value)
'''

class Image(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.dir = Blender.Get('uscriptsdir')
        self.file = ''
        self.x_zoom = 1.0
        self.y_zoom = 1.0
        self.x_clip = 0
        self.y_clip = 0
        self.clip_width = -1
        self.clip_height = -1
        self.image_block = None
        super(Image, self).__init__(**kvargs)
        
        # TODO: it would be safer to check the file header
        if self.file.endswith('svg'):
            self.dir = get_icons_dir()
            
            source_dir = Blender.Get('uscriptsdir')
            svg_path = find_file_path(source_dir, self.file)
            
            png_name = change_extension(self.file, 'png')
            png_path = os.path.join(self.dir, png_name)
            
            convert_svg_to_png(svg_path, png_path, self.width, self.height)
            
            self.file = png_name # use png version from now on
        
        self.image_block = load_image(self.dir, self.file)
        self.set_element_dimensions()
    
    def load_image(self, name):
        self.image_block = load_image(self.dir, name)
        self.set_element_dimensions()
    
    def set_element_dimensions(self):
        if self.image_block:
            width, height = self.image_block.getSize()
            
            if self.height and self.width:
                self.height = self.height
                self.width = self.width
            elif self.height:
                self.height = self.height
                self.width = float(self.height) / height * width
            elif self.width:
                self.height = float(self.width) / width * height
                self.width = self.width
            else:
                self.height = height
                self.width = width
    
    @enable_alpha
    def render(self):
        if self.image_block:
            width, height = self.image_block.getSize()
            self.x_zoom = float(self.width) / width
            self.y_zoom = float(self.height) / height
            
            Draw.Image(self.image_block, self.x, self.y,
                       self.x_zoom, self.y_zoom, self.x_clip, self.y_clip,
                       self.clip_width, self.clip_height)

class Icon(AbstractBlenderElement):
    def __init__(self, **kvargs):
        """ Adapted from txtPyBrowser114j.py by Remigiusz Fiedler """
        def get_icon_position(index):
            row = index / 25
            col = index - (row * 25)
            return row, col
        
        self.file = 'blenderbuttons.png'
        super(Icon, self).__init__(**kvargs)
        
        index = BLENDER_ICONS.index(self.name)
        row, col = get_icon_position(index)
        self.width = 20
        self.height = 21
        self.clip_x = col * self.width + 3
        self.clip_y = row * self.height + 3
        self.clip_width = 15
        self.clip_height = 15
        
        uscriptsdir = Blender.Get('uscriptsdir')
        self.image_block = load_image(uscriptsdir, self.file)
    
    @enable_alpha
    def render(self):
        Draw.Image(self.image_block, self.x, self.y, 1.0, 1.0, self.clip_x,
                   self.clip_y, self.clip_width, self.clip_height)
