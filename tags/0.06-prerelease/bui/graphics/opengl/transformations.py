# -*- coding: utf-8 -*-
from OpenGL.GL import glRotatef, glScalef, glTranslatef

def mirror_x():
    glScalef(-1.0, 1.0, 1.0)

def mirror_y():
    glScalef(1.0, -1.0, 1.0)

def mirror_z():
    glScalef(1.0, 1.0, -1.0)

def rotate(angle=0.0, x=0.0, y=0.0, z=0.0):
    glRotatef(angle, x, y, z)

def scale(x=0.0, y=0.0, z=0.0):
    glScalef(x, y, z)

def translate(x=0.0, y=0.0, z=0.0):
    glTranslatef(x, y, z)
