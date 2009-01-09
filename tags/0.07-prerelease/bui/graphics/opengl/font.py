# -*- coding: utf-8 -*-
from __future__ import with_statement

try:
    from FTGL import TextureFont
except ImportError:
    print "Missing FTGL. Labels won't work!"

from bui.utils.coordinate import Coordinate
from bui.utils.path import get_font_path
from color import set_color
from decorators import enable_alpha, enable_texture2d
from transformations import mirror_y, translate
from with_statements import matrix_stack

class Font():
    def __init__(self, font_name):
        font_path = get_font_path(font_name)
        self.font = TextureFont(font_path)
    
    def get_bounding_box(self, parent):
        class BoundingBox():
            def __init__(self, bbox=None):
                self.bottom_left = Coordinate(x=bbox[0], y=bbox[1])
                self.top_right = Coordinate(x=bbox[3], y=bbox[4])
            
            def get_width(self):
                return self.top_right.x - self.bottom_left.x
            width = property(get_width)
            
            def get_height(self):
                return self.top_right.y - self.bottom_left.y
            height = property(get_height)
        
        if parent.height > 0:
            self.font.FaceSize(parent.height)
            bbox = self.font.BBox(parent.label)
            return BoundingBox(bbox)
    
    @enable_alpha
    @enable_texture2d
    def render(self, parent):
        # FIXME: bit of a hack but can't allow too small labels to be drawn
        if parent.height > 0:
            self.font.FaceSize(parent.height)
            
            set_color(parent.color, parent.alpha)
            
            with matrix_stack():
                # note that FTGL uses OpenGL drawing convention by default!
                translate(parent.x, parent.y + parent.height)
                mirror_y()
                
                self.font.Render(parent.label)
