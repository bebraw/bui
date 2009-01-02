# -*- coding: utf-8 -*-
from OpenGL.GL import glLoadIdentity, glMatrixMode, GL_MODELVIEW, GL_PROJECTION, GL_TEXTURE

MODELVIEW = GL_MODELVIEW
PROJECTION = GL_PROJECTION
TEXTURE = GL_TEXTURE

def load_identity_matrix():
    glLoadIdentity()

def set_matrix_mode(mode):
    glMatrixMode(mode)
