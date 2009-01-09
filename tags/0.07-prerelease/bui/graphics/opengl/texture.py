# -*- coding: utf-8 -*-
from OpenGL.GL import glBindTexture, GL_TEXTURE_2D

def bind_2d_texture(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
