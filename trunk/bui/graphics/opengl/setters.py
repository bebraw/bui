# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def set_color(color, alpha=1.0):
    glColor4f(*color + [alpha])
