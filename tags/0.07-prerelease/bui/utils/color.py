# -*- coding: utf-8 -*-
from random import random

# TODO: should implement nice Color class and use that internally
# see http://www.python.org/doc/2.6/library/colorsys.html !!!
# there should be some nice way to convert colors to other systems
# Note that colors should treat their channels as floats [0.0, 1.0]
# internally. if integers are passed/set, assume 0-255 range and convert
# to internal representation? might give warning about this?
# Note that alpha is separated from color atm.

# default color system used!
class RGBColor():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class HSVColor():
    def __init__(self, h, s, v):
        self.h = h
        self.s = s
        self.v = v

# TODO: should return color
# TODO: could add more options (center of probability distribution, variance etc.)
# -> make it possible to give a func describing distribution?
def generate_color():
    return (random(), random(), random())

# TODO: add more implementations for different systems? (don't rely only on gtk)
def pick_color_at_current_mouse_location():
    ''' adapted from wpicker-applet '''
    try:
        import gtk
    except ImportError:
        print 'color picker not available as gtk cannot be found!'
        return None
    
    display = gtk.gdk.display_get_default()
    screen = display.get_default_screen()
    root_window = screen.get_root_window()
    x, y, mods = root_window.get_pointer()
    
    img = root_window.get_image(int(x), int(y), 1, 1)
    pixel = img.get_pixel(0, 0)
    color_map = screen.get_system_colormap()
    color = color_map.query_color(pixel)
    
    red = color.red / 256.0
    green = color.green / 256.0
    blue = color.blue / 256.0
    return ("#%0.2x%0.2x%0.2x" % (red, green, blue))
    # should return RGBColor instead
