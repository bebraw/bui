# -*- coding: utf-8 -*-

def mirror_x():
    ogl.glScalef(-1.0, 1.0, 1.0)

def mirror_y():
    ogl.glScalef(1.0, -1.0, 1.0)

def mirror_z():
    ogl.glScalef(1.0, 1.0, -1.0)

def rotate(angle=0.0, x=0.0, y=0.0, z=0.0):
    ogl.glRotatef(angle, x, y, z)

def scale(x=0.0, y=0.0, z=0.0):
    ogl.glScalef(x, y, z)

def translate(x=0.0, y=0.0, z=0.0):
    ogl.glTranslatef(x, y, z)
