# -*- coding: utf-8 -*-
from OpenGL.GLUT import glutKeyboardFunc, glutKeyboardUpFunc

from bui.backend.event import BaseEventManager

class EventManager(BaseEventManager):
    def __init__(self, root_layout, keys, events):
        super(EventManager, self).__init__(root_layout, keys, events)
        
        glutKeyboardFunc(self.key_pressed)
        glutKeyboardUpFunc(self.key_released)
    
    def key_pressed(self, key, x, y):
        self.key_event(key, pressed=True)
    
    def key_released(self, key, x, y):
        self.key_event(key, pressed=False)
