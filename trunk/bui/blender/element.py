# -*- coding: utf-8 -*-
import os

try:
    import cairo
    import rsvg
except ImportError:
    print "Missing cairo or rsvg. Image with svg extension won't work!"

try:
    import Blender
    from Blender import BGL, Draw
except ImportError:
    pass

from bui.abstract import AbstractElement

from icons import BLENDER_ICONS

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
    def __init__(self, **kvargs):
        self.value = ''
        super(TextBox, self).__init__(**kvargs)
    
    def render(self, coord):
        self.textbox = Draw.String(self.name + ': ', self.event, coord.x, coord.y - self.height,
                                   self.width, self.height, self.value, self.max_input_length,
                                   self.tooltip, self.update_value)

class ToggleButton(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = False
        super(ToggleButton, self).__init__(**kvargs)
    
    def render(self, coord):
        self.togglebutton = Draw.Toggle(self.name, self.event, coord.x, coord.y - self.height, self.width,
                                        self.height, self.value, self.tooltip, self.update_value)

class PushButton(AbstractBlenderElement):
    def render(self, coord):
        self.pushbutton = Draw.PushButton(self.name, self.event, coord.x, coord.y - self.height, self.width,
                                          self.height, self.tooltip)

class Menu(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0
        super(Menu, self).__init__(**kvargs)
    
    def render(self, coord):
        self.menu = Draw.Menu(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                         self.value, self.tooltip, self.update_value)

class Slider(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0.0
        super(Slider, self).__init__(**kvargs)
    
    def render(self, coord):
        self.slider = Draw.Slider(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                                  self.value, self.min, self.max, False, self.tooltip, self.update_value)

class Number(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.range = 0 # no clickstep
        self.precision = 0.0 # 4 decimals
        self.value = 0.0
        super(Number, self).__init__(**kvargs)
        self.value = float(self.value)
    
    def render(self, coord):
        try:
            self.number = Draw.Number(self.name, self.event, coord.x, coord.y - self.height, self.width,
                                      self.height, self.value, self.min, self.max, self.tooltip,
                                      self.update_value, self.range, self.precision)
        except: # needed for backwards compatibility (no range and precision in 2.48a)
            self.number = Draw.Number(self.name, self.event, coord.x, coord.y - self.height, self.width,
                                      self.height, self.value, self.min, self.max, self.tooltip,
                                      self.update_value)

class IntNumber(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0
        super(IntNumber, self).__init__(**kvargs)
    
    def render(self, coord):
        self.number = Draw.Number(self.name, self.event, coord.x, coord.y - self.height, self.width, self.height,
                                  int(self.value), int(self.min), int(self.max), self.tooltip, self.update_value)

class ColorPicker(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = (0.0, 0.0, 0.0, )
        super(ColorPicker, self).__init__(**kvargs)
    
    def render(self, coord):
        self.colorpicker = Draw.ColorPicker(self.event, coord.x, coord.y - self.height, self.width, self.height,
                                            self.value, self.tooltip, self.update_value)

'''
FIXME: self.update_value callback doesn't get called for some reason -> value does not get updated
class Normal(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = (1.0, 1.0, 1.0, )
        super(Normal, self).__init__(**kvargs)
    
    def render(self, coord):
        self.normal = Draw.Normal(self.event, coord.x, coord.y - self.height, self.width, self.height,
                                  self.value, self.tooltip, self.update_value)
'''

def load_image(root_dir, file_name):
    file_path = find_file_path(root_dir, file_name)
    
    if file_path:
        return Blender.Image.Load(file_path)

# TODO: move to utils
def enable_alpha(func):
    def wrapper(self,*args,**kvargs):
        BGL.glEnable(BGL.GL_BLEND)
        BGL.glBlendFunc(BGL.GL_SRC_ALPHA, BGL.GL_ONE_MINUS_SRC_ALPHA)
        try:
            return func(self,*args,**kvargs)
        finally:
            BGL.glDisable(BGL.GL_BLEND)
    
    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__ = func.__doc__
    return wrapper

# TODO: move to utils
def get_icons_dir():
    return Blender.Get('tempdir')
    #return os.path.join(tempdir, 'tmp_icons')

# TODO: move to utils
def change_extension(file_name, new_extension):
    extension_index = file_name.rfind('.')
    base_name = file_name[:extension_index]
    return base_name + '.' + new_extension

# TODO: move to utils
def convert_svg_to_png(source_file, target_file, width, height):
    """ Adapted from http://guillaume.segu.in/blog/code/43/svg-to-png/ """
    svg = rsvg.Handle(file=source_file)
    
    if width:
        ratio = float(width) / svg.props.width
        height = int(ratio * svg.props.height)
    else:
        width = svg.props.width
    
    if height:
        ratio = float(height) / svg.props.height
        width = int(ratio * svg.props.width)
    else:
        height = svg.props.height
    
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(surface)
    
    wscale = float(width) / svg.props.width
    hscale = float(height) / svg.props.height
    cr.scale(wscale, hscale)
    
    svg.render_cairo(cr)
    surface.write_to_png(target_file)

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
    
    def set_element_dimensions(self):
        if self.image_block:
            width, height = self.image_block.getSize()
            
            self.height = self.height if self.height else height
            self.width = self.width if self.width else width
    
    @enable_alpha
    def render(self, coord):
        if self.image_block:
            width, height = self.image_block.getSize()
            self.x_zoom = float(self.width) / width
            self.y_zoom = float(self.height) / height
            
            Draw.Image(self.image_block, coord.x, coord.y - self.height,
                       self.x_zoom, self.y_zoom, self.x_clip, self.y_clip,
                       self.clip_width, self.clip_height)

class Icon(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.file = 'blenderbuttons.png'
        super(Icon, self).__init__(**kvargs)
        
        uscriptsdir = Blender.Get('uscriptsdir')
        self.image_block = load_image(uscriptsdir, self.file)
    
    @enable_alpha
    def render(self, coord):
        """ Adapted from txtPyBrowser114j.py by Remigiusz Fiedler """
        def get_icon_position(index):
            row = index / 25
            col = index - (row * 25)
            return row, col
        
        index = BLENDER_ICONS.index(self.name)
        row, col = get_icon_position(index)
        dx, dy, = 20, 21
        clipx = col * dx + 3
        clipy = row * dy + 3
        clipw, cliph = 15,15
        
        Draw.Image(self.image_block, coord.x, coord.y - dy, 1.0, 1.0, clipx, clipy, clipw, cliph)
