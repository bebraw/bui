# -*- coding: utf-8 -*-
from OpenGL.GLUT import glutKeyboardFunc, glutKeyboardUpFunc
from bui.backend.event import BaseEventManager
from timer import Timer

class EventManager(BaseEventManager):
    def __init__(self, root_elem, keys, events):
        super(EventManager, self).__init__(root_elem, keys, events)
        
        glutKeyboardFunc(self.key_pressed)
        glutKeyboardUpFunc(self.key_released)
        
        self.timers = []
    
    def key_pressed(self, key, x, y):
        print key, x, y
        self.key_event(key, pressed=True)
    
    def key_released(self, key, x, y):
        self.key_event(key, pressed=False)
    
    # should go elsewhere?
    def create_timer(self, func, interval):
        ''' interval in seconds! '''
        self.timers.append(Timer(self.root_elem, func, interval))
