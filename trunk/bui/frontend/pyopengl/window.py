# -*- coding: utf-8 -*-
from OpenGL.GLUT import *

from bui.backend.window import BaseWindow, BaseWindowContainer, BaseWindowManager
from bui.graphics.opengl.color import clear_color
from bui.graphics.opengl.projections import setup_2D_projection
from timer import TimerManager

# evil hack to modify serializer namespace!!!
import element

class WindowManager(BaseWindowManager):
    def __init__(self, configuration, structure_document=None, hotkeys=None, events=None,
                 timers=None, constraints=None, initializers=None):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) # GLUT_DEPTH needed???
        
        super(WindowManager, self).__init__(configuration, structure_document, hotkeys,
                                            events, timers, constraints, initializers)
        
        glutDisplayFunc(self.redraw)
    
    def initialize_timers(self):
        self.timer_manager = TimerManager(self.windows[0], self.timers) # XXX: passing window in a nasty way
    
    def initialize_windows(self):
        self.windows = []
        self.windows.append(Window(self.name, self.label, self.width, self.height, self.show_fps,
                                   self.logging, self.alignment, self.element_height,
                                   self.start_timers, self.structure_document, self.structure,
                                   self.hotkeys, self.initializer))
    
    def get_mouse_coordinates(self):
        return (0, 0) # TODO: implement
    
    def redraw(self):
        super(WindowManager, self).redraw()
        glutSwapBuffers() 
    
    def run(self):
        super(WindowManager, self).run()
        glutMainLoop()

class WindowContainer(BaseWindowContainer):
    pass

class Window(BaseWindow):
    def __init__(self, name, label, width, height, show_fps, logging, alignment,
                 element_height, start_timers, structure_document, structure,
                 hotkeys, initializer):
        super(Window, self).__init__(name, label, width, height, show_fps,
                                         logging, alignment, element_height,
                                         start_timers, structure_document,
                                         structure, hotkeys, initializer)
        glutInitWindowSize(self.width, self.height)
        
        # the window starts at the upper left corner of the screen
        # TODO: hook up alignment with this!
        glutInitWindowPosition(0, 0)
        
        self.window = glutCreateWindow(name) # might work even without self (even without assignment???)
        
        # glutFullScreen() # TODO: hook up this with conf!
        
        glutReshapeFunc(self.resize)
        glutVisibilityFunc(self.visibility)
        
        setup_2D_projection(self.width, self.height)
    
    def resize(self, width, height):
        self.height = height
        self.width = width
        
        setup_2D_projection(self.width, self.height)
    
    def visibility(self, visible):
        idle_func = None
        
        if visible:
            idle_func = self.idle
        
        glutIdleFunc(idle_func)
    
    def idle(self):
        glutPostRedisplay()
    
    def redraw(self):
        clear_color() # TODO: provide bg color. this should probably happen on lower level (handles background automagically!)
        super(Window, self).redraw()
