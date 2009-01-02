# -*- coding: utf-8 -*-
from OpenGL.GL import glBegin, glEnd, glPopMatrix, glPushMatrix

class matrix_stack():
    def __enter__(self):
        glPushMatrix()
    
    def __exit__(self, type, value, traceback):
        glPopMatrix()

class mode():
    def __init__(self, statement):
        self.statement = statement
    
    def __enter__(self):
        glBegin(self.statement)
    
    def __exit__(self, type, value, traceback):
        glEnd()
