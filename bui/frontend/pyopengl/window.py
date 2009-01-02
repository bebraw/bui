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
        
        #glutTimerFunc(1000, self.test_timer, 5) # test
        
        setup_2D_projection(self.width, self.height)
    
    def test_timer(self, val=None):
        print 'timer triggered'
        #print val
        from time import localtime
        time_list = localtime()[3:6]
        time_list_items_as_string = ['%02d:' % i for i in time_list]
        current_time = ''.join(time_list_items_as_string)[:-1]
        print current_time
        glutTimerFunc(1000, self.test_timer, 5) # test
    
    def get_mouse_coordinates(self):
        return (0, 0) # TODO: implement
    
    def resize(self, width, height):
        self.height = height
        self.width = width
        
        setup_2D_projection(self.width, self.height) # to projections.py
