# -*- coding: utf-8 -*-

def set_color(color, alpha=1.0):
    ogl.glColor4f(*color + [alpha])
