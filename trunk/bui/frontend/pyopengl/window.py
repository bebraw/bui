# -*- coding: utf-8 -*-
from OpenGL.GLUT import *

from bui.backend.window import BaseWindowManager
from bui.graphics.opengl.projections import setup_2D_projection

# TODO: implement Window (clean up abstract, root aOb should have Window as parent (no more common))
# to make it possible to use multiple windows

class WindowManager(BaseWindowManager):
    def __init__(self, name, width, height):
        super(WindowManager, self).__init__(name, width, height)
        
        glutInitWindowSize(self.width, self.height)
        
        # the window starts at the upper left corner of the screen
        # TODO: make this configurable (conf file!)
        glutInitWindowPosition(0, 0)
        
        self.window = glutCreateWindow(name)
        
        # glutFullScreen() # TODO: add option for full screen
        
        glutReshapeFunc(self.resize)
        
        setup_2D_projection(self.width, self.height)
    
    def get_mouse_coordinates(self):
        return (0, 0) # TODO: implement
    
    def resize(self, width, height):
        self.height = height
        self.width = width
        
        setup_2D_projection(self.width, self.height) # to projections.py
