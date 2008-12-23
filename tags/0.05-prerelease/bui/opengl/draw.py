# -*- coding: utf-8 -*-

def draw_line(line_width, color, x1, y1, x2, y2):
    ogl.glLineWidth(line_width)
    ogl.glColor3f(*color)
    ogl.glBegin(ogl.GL_LINES)
    ogl.glVertex2f(x1, y1)
    ogl.glVertex2f(x2, y2)
    ogl.glEnd()

def draw_rectangle(color, x1, y1, x2, y2):
    ogl.glColor3f(*color)
    ogl.glRectf(x1, y1, x2, y2)
