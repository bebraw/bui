# -*- coding: utf-8 -*-
import sys

from OpenGL.GLUT import glutDisplayFunc, glutIdleFunc, glutMainLoop, glutSwapBuffers

from bui.backend.application import BaseApplication

from event import EventManager
from window import WindowManager

class Application(BaseApplication):
    def __init__(self, structure, keys, events=None, constraints=None,
                 ui_initializer=None, element_height=20, window_name='',
                 window_width=640, window_height=480):
        super(Application, self).__init__(structure, keys, events,
                                          constraints, ui_initializer, element_height)
        
        self.window_manager = WindowManager(window_name, window_width, window_height)
        self.event_manager = EventManager(self.root_container, keys, events)
        
        glutDisplayFunc(self.gui)
        glutIdleFunc(self.gui)
    
    def gui(self):
        super(Application, self).gui()
        glutSwapBuffers() # double buffered drawing (separate this to window manager?)
    
    def run(self):
        super(Application, self).run()
        glutMainLoop()
