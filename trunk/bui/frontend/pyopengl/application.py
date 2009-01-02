# -*- coding: utf-8 -*-
import sys
from OpenGL.GLUT import *
from bui.backend.application import BaseApplication
from bui.graphics.opengl.color import clear_color

# trigger element to modify serializer namespace. could be neater...
import element

from event import EventManager
from window import WindowManager

class Application(BaseApplication):
    def __init__(self, structure, keys, events=None, constraints=None,
                 ui_initializer=None, element_height=20, window_name='',
                 window_width=640, window_height=480):
        super(Application, self).__init__(structure, keys, events,
                                          constraints, ui_initializer, element_height)
        
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        
        self.window_manager = WindowManager(window_name, window_width, window_height)
        self.root_layout.common.window_manager = self.window_manager
        
        self.event_manager = EventManager(self.root_layout, keys, events)
        
        glutDisplayFunc(self.redraw)
        glutIdleFunc(self.redraw) # uncomment this if timers are added
    
    def redraw(self):
        clear_color() # TODO: provide bg color
        super(Application, self).redraw()
        
        # use double buffered drawing
        glutSwapBuffers() 
    
    def run(self):
        super(Application, self).run()
        glutMainLoop()
