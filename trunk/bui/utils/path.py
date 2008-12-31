# -*- coding: utf-8 -*-
import os

def get_font_path(font_name):
    import bui
    bui_path = os.path.dirname(bui.__file__)
    bui_root_path = os.path.split(bui_path)[0]
    return os.path.join(bui_root_path, 'fonts', font_name) + '.' + 'ttf'
