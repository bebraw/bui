# -*- coding: utf-8 -*-

def enable_alpha(func):
    def wrapper(self,*args,**kvargs):
        ogl.glEnable(ogl.GL_BLEND)
        ogl.glBlendFunc(ogl.GL_SRC_ALPHA, ogl.GL_ONE_MINUS_SRC_ALPHA)
        
        try:
            return func(self,*args,**kvargs)
        finally:
            ogl.glDisable(ogl.GL_BLEND)
    
    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__ = func.__doc__
    return wrapper
