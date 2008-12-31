# -*- coding: utf-8 -*-
try:
    from FTGL import TextureFont
except ImportError:
    print "Missing FTGL. Labels won't work!"

from bui.utils.path import get_font_path

class Font():
    def __init__(self, name):
        font_path = get_font_path(name)
        self.font = TextureFont(font_path)
    
    def render(self, text, height):
        self.font.FaceSize(height)
        self.font.Render(text)
