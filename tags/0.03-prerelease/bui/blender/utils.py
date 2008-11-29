# -*- coding: utf-8 -*-
import os

try:
    import Blender
    from Blender import BGL, Image
except ImportError:
    pass

try:
    import cairo
    import rsvg
except ImportError:
    print "Missing cairo or rsvg. Image with svg extension won't work!"

def find_file_path(root_dir, file_name):
    """ Returns path to given file_name with file_name appended. """
    for root, dirs, files in os.walk(root_dir):
        if file_name in files:
            return os.path.join(root, file_name)

def load_image(root_dir, file_name):
    file_path = find_file_path(root_dir, file_name)
    
    if file_path:
        return Image.Load(file_path)

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

def get_icons_dir():
    return Blender.Get('tempdir')
    #return os.path.join(tempdir, 'tmp_icons')

def change_extension(file_name, new_extension):
    extension_index = file_name.rfind('.')
    base_name = file_name[:extension_index]
    return base_name + '.' + new_extension

def convert_svg_to_png(source_file, target_file, width, height):
    """ Adapted from http://guillaume.segu.in/blog/code/43/svg-to-png/ """
    if not source_file:
        return
    
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
