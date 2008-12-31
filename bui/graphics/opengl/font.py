# -*- coding: utf-8 -*-
from __future__ import with_statement

try:
    from FTGL import TextureFont
except ImportError:
    print "Missing FTGL. Labels won't work!"

from bui.utils.path import get_font_path
from decorators import enable_alpha, enable_texture2d
from setters import set_color
from transformations import mirror_y, translate
from with_statements import matrix_stack

class Font():
    def __init__(self, parent_object):
        self.parent_object = parent_object
    
    @enable_alpha
    @enable_texture2d
    def render(self):
        font_path = get_font_path(self.parent_object.font_name)
        font = TextureFont(font_path)
        font.FaceSize(self.parent_object.height)
        
        set_color(self.parent_object.color, self.parent_object.alpha)
        
        with matrix_stack():
            # note that FTGL uses OpenGL drawing convention by default!
            translate(self.parent_object.x, self.parent_object.y + self.parent_object.height)
            mirror_y()
            
            font.Render(self.parent_object.name) # TODO: self.parent_object.text better?
