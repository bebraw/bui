# -*- coding: utf-8 -*-
from OpenGL.GL import glClear, glClearColor, glColor4f, GL_COLOR_BUFFER_BIT

def clear_color(color=None):
    if color:
        if len(color) == 3:
            color.append(1.0) # default alpha. could handle color neater! -> abstract!
        
        glClearColor(*color) # TODO: handle color better (validate etc.)
    glClear(GL_COLOR_BUFFER_BIT)

def set_color(color=[0.0, 0.0, 0.0], alpha=1.0):
    glColor4f(*color + [alpha])
