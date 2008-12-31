# -*- coding: utf-8 -*-
import sys

from OpenGL.GL import glClear, glClearColor, GL_COLOR_BUFFER_BIT
from OpenGL.GLUT import glutDisplayFunc, glutIdleFunc, glutMainLoop, glutSwapBuffers

from bui.backend.application import BaseApplication

# trigger element to add modify serializer namespace. could be neater...
import element

from event import EventManager
from window import WindowManager

class Application(BaseApplication):
    def __init__(self, structure, keys, events=None, constraints=None,
                 ui_initializer=None, element_height=20, window_name='',
                 window_width=640, window_height=480):
        super(Application, self).__init__(structure, keys, events,
                                          constraints, ui_initializer, element_height)
        
        self.window_manager = WindowManager(window_name, window_width, window_height)
        self.root_container.common.window_manager = self.window_manager
        
        self.event_manager = EventManager(self.root_container, keys, events)
        
        glutDisplayFunc(self.redraw)
        #glutIdleFunc(self.redraw) # uncomment this if timers are added
    
    def redraw(self):
        #glClearColor(.3, .3, .3, 0) # *bg_color + 0.0
        glClear(GL_COLOR_BUFFER_BIT)
        
        super(Application, self).redraw()
        
        # double buffered drawing
        glutSwapBuffers() 
    
    def run(self):
        super(Application, self).run()
        glutMainLoop()
