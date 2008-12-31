# -*- coding: utf-8 -*-

class MatrixStack():
    def __enter__(self):
        ogl.glPushMatrix()
    
    def __exit__(self, type, value, traceback):
        ogl.glPopMatrix()
