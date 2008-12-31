# -*- coding: utf-8 -*-
from OpenGL.GL import *

def set_color(color=[0.0, 0.0, 0.0], alpha=1.0):
    glColor4f(*color + [alpha])
