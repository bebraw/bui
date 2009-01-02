# -*- coding: utf-8 -*-
from OpenGL.GL import glViewport

def viewport(x, y, width, height):
    glViewport(x, y, width, height)
