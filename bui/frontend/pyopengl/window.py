# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from bui.backend.window import BaseWindowManager

class WindowManager(BaseWindowManager):
    def __init__(self, name, width, height):
        super(WindowManager, self).__init__(name, width, height)
        
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0) # the window starts at the upper left corner of the screen
        
        self.window = glutCreateWindow(name)
        
        # glutFullScreen() # add option for full screen later
        
        glutReshapeFunc(self.resize)
        
        self.setup_2D_projection()
    
    def get_mouse_coordinates(self):
        return (0, 0) # TODO: implement
    
    def resize(self, width, height):
        self.height = height
        self.width = width
        print width, height
        self.setup_2D_projection()
    
    def setup_2D_projection(self):
        ''' Adapted from http://basic4gl.wikispaces.com/2D+Drawing+in+OpenGL '''
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        glViewport(0, 0, self.width, self.height)
        
        glOrtho(0, self.width, self.height, 0, 0, 1)
        glDisable(GL_DEPTH_TEST)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()
        
        # Displacement trick for exact pixelization
        glTranslatef(0.375, 0.375, 0)
