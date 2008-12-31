# -*- coding: utf-8 -*-

def draw_line(line_width, color, x1, y1, x2, y2):
    ogl.glLineWidth(line_width)
    ogl.glColor3f(*color) # TODO: should use set_color
    ogl.glBegin(ogl.GL_LINES) # TODO: replace with "with"
    ogl.glVertex2f(x1, y1)
    ogl.glVertex2f(x2, y2)
    ogl.glEnd()

# TODO: convert to decorator!
def check_input(x1, y1, x2, y2, width, height):
    ret_x = x2 or x1 + (width or 0)
    ret_y = y2 or y1 + (height or 0)
    
    return ret_x, ret_y

def draw_rectangle(color, x1, y1, x2=None, y2=None, width=None, height=None):
    x2, y2 = check_input(x1, y1, x2, y2, width, height)
    
    ogl.glColor3f(*color) # TODO: should use set_color
    ogl.glRectf(x1, y1, x2, y2)

def draw_textured_rectangle(texture, x1, y1, x2=None, y2=None, width=None, height=None):
    x2, y2 = check_input(x1, y1, x2, y2, width, height)
    
    ogl.glBindTexture(ogl.GL_TEXTURE_2D, texture);
    
    ogl.glBegin(ogl.GL_QUADS) # TODO: replace with "with"
    ogl.glTexCoord2f(0.0, 0.0)
    ogl.glVertex2f(x1, y1)
    ogl.glTexCoord2f(1.0, 0.0)
    ogl.glVertex3f(x2, y1)
    ogl.glTexCoord2f(1.0, 1.0)
    ogl,glVertex3f(x2, y2)
    ogl.glTexCoord2f(0.0, 1.0)
    ogl.glVertex3f(x1, y2)
    BGL.glEnd()
