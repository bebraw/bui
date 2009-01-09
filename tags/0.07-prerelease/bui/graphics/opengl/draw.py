# -*- coding: utf-8 -*-
from __future__ import with_statement
from OpenGL.GL import glLineWidth, glRectf, glTexCoord2f, glVertex2f, \
                      GL_LINES, GL_QUADS
from color import set_color
from texture import bind_2d_texture
from with_statements import mode

def draw_line(line_width, color, x1, y1, x2, y2):
    glLineWidth(line_width)
    set_color(color)
    
    with mode(GL_LINES):
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)

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
    
    bind_2d_texture(texture)
    draw_textured_quad(((x1, y1), (x2, y1), (x2, y2), (x1, y2)))

def draw_textured_quad(coords):
    tex_coords = ((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
    
    with mode(GL_QUADS):
        for i in range(4):
            tex_x = tex_coords[i][0]
            tex_y = tex_coords[i][1]
            glTexCoord2f(tex_x, tex_y)
            
            x = coords[i][0]
            y = coords[i][1]
            glVertex2f(x, y)
