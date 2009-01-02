# -*- coding: utf-8 -*-
from OpenGL.GL import glBlendFunc, glDisable, glEnable, GL_BLEND, \
                      GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_TEXTURE_2D

def enable_alpha(func):
    def wrapper(self, *args, **kvargs):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        try:
            return func(self, *args, **kvargs)
        finally:
            glDisable(GL_BLEND)
    
    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__ = func.__doc__
    return wrapper

def enable_texture2d(func):
    def wrapper(self, *args, **kvargs):
        glEnable(GL_TEXTURE_2D)
        
        try:
            return func(self, *args, **kvargs)
        finally:
            glDisable(GL_TEXTURE_2D)
    
    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__ = func.__doc__
    return wrapper
