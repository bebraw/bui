# -*- coding: utf-8 -*-
from OpenGL.GLUT import *
from bui.backend.window import BaseWindow, BaseWindowContainer, BaseWindowManager
from bui.graphics.opengl.color import clear_color
from bui.graphics.opengl.projections import setup_2D_projection
from event import EventManager
from timer import TimerManager

class WindowManager(BaseWindowManager):
    def __init__(self, configuration, structure_document=None, hotkeys=None, events=None,
                 timers=None, constraints=None, initializers=None):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        
        super(WindowManager, self).__init__(configuration, structure_document, hotkeys,
                                            events, timers, constraints, initializers)
        
        glutDisplayFunc(self.redraw)
    
    def initialize_timers(self):
        self.timer_manager = TimerManager(self.windows[0], self.timers) # XXX: passing window in a nasty way
    
    def initialize_windows(self):
        self.windows = []
        self.windows.append(Window(self.name, self.label, self.width, self.height, self.show_fps,
                                   self.logging, self.alignment,
                                   self.default_node_width, self.default_node_height,
                                   self.bg_color,
                                   self.start_timers, self.structure_document, self.structure,
                                   self.hotkeys, self.initializer, self.events))
    
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
                 default_node_width, default_node_height, bg_color, start_timers,
                 structure_document, structure,
                 hotkeys, initializer, events):
        super(Window, self).__init__(name, label, width, height, show_fps,
                                         logging, alignment,
                                         default_node_width, default_node_height,
                                         bg_color,
                                         start_timers, structure_document,
                                         structure, hotkeys, initializer, events)
        
        glutInitWindowSize(self.width, self.height)
        
        # the window starts at the upper left corner of the screen
        # TODO: hook up alignment with this!
        glutInitWindowPosition(0, 0)
        
        self.window = glutCreateWindow(self.label) # check if window ID is actually needed for something
        
        # glutFullScreen() # TODO: hook up this with conf!
        
        glutReshapeFunc(self.resize)
        glutVisibilityFunc(self.visibility)
        
        self.event_manager = EventManager(self.root_layout, self.hotkeys, self.events)
        
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
        clear_color(self.bg_color)
        super(Window, self).redraw()
