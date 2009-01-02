# -*- coding: utf-8 -*-
from __future__ import with_statement

try:
    from FTGL import TextureFont
except ImportError:
    print "Missing FTGL. Labels won't work!"

from bui.utils.coordinate import Coordinate
from bui.utils.path import get_font_path
from decorators import enable_alpha, enable_texture2d
from setters import set_color
from transformations import mirror_y, translate
from with_statements import matrix_stack

# TODO: trigger update to self.font if self.parent_object.font_name changes!
# TODO: same thing with self.parent_object.height!!!

class Font():
    def __init__(self, parent_object):
        self.parent_object = parent_object
        font_path = get_font_path(self.parent_object.font_name)
        self.font = TextureFont(font_path)
        self.font.FaceSize(self.parent_object.height)
    
    def get_bounding_box(self):
        class BoundingBox():
            def __init__(self, bbox):
                self.bottom_left = Coordinate(x=bbox[0], y=bbox[1])
                self.top_right = Coordinate(x=bbox[3], y=bbox[4])
            
            def get_width(self):
                return self.top_right.x - self.bottom_left.x
            width = property(get_width)
            
            def get_height(self):
                return self.top_right.y - self.bottom_left.y
            height = property(get_height)
        self.font.FaceSize(self.parent_object.height) # TODO: refactor out
        bbox = self.font.BBox(self.parent_object.name)
        return BoundingBox(bbox)
    
    @enable_alpha
    @enable_texture2d
    def render(self):
        self.font.FaceSize(self.parent_object.height) # TODO: refactor out
        
        set_color(self.parent_object.color, self.parent_object.alpha)
        
        with matrix_stack():
            # note that FTGL uses OpenGL drawing convention by default!
            translate(self.parent_object.x, self.parent_object.y + self.parent_object.height)
            mirror_y()
            
            self.font.Render(self.parent_object.label)
