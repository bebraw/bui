# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from setters import set_color

def draw_line(line_width, color, x1, y1, x2, y2):
    glLineWidth(line_width)
    set_color(color)
    glBegin(GL_LINES) # TODO: replace with "with"
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

# TODO: convert to decorator!
def check_input(x1, y1, x2, y2, width, height):
    ret_x = x2 or x1 + (width or 0)
    ret_y = y2 or y1 + (height or 0)
    
    return ret_x, ret_y

def draw_rectangle(color, x1, y1, x2=None, y2=None, width=None, height=None):
    x2, y2 = check_input(x1, y1, x2, y2, width, height)
    
    set_color(color)
    glRectf(x1, y1, x2, y2)

def draw_textured_rectangle(texture, x1, y1, x2=None, y2=None, width=None, height=None):
    x2, y2 = check_input(x1, y1, x2, y2, width, height)
    
    glBindTexture(GL_TEXTURE_2D, texture);
    
    glBegin(GL_QUADS) # TODO: replace with "with"
    glTexCoord2f(0.0, 0.0)
    glVertex2f(x1, y1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x2, y1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x2, y2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x1, y2)
    glEnd()
