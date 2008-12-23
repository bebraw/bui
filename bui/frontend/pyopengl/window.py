# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from bui.backend.window import BaseWindowManager

from bui.utils.coordinate import Coordinate

# to graphics?
# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):                # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    glClearDepth(1.0)                    # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)                # Enables Depth Testing
    glShadeModel(GL_SMOOTH)                # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

class WindowManager(BaseWindowManager):
    def __init__(self, name, width, height):
        self.coordinates = [0, 0, width, height]
        #self.width = width
        #self.height = height
        
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0) # the window starts at the upper left corner of the screen
        
        self.window = glutCreateWindow(name)
        
        # glutFullScreen() # add option for full screen later
        
        glutReshapeFunc(self.resize)
        
        InitGL(width, height)
    
    def get_coordinates(self):
        return self.coordinates # get rid of get_coordinates in base class???
    
    def get_mouse_coordinates(self):
        xmin, ymin, xmax, ymax = self.get_coordinates()
        mouse_x, mouse_y = Window.GetMouseCoords()
        
        return Coordinate(mouse_x-xmin, mouse_y-ymin)
    
    # convert this to use 2d viewport code (see cassopi)
    def resize(self, width, height):
        height = max(height, 1)
        
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
