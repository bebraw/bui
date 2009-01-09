# -*- coding: utf-8 -*-
from OpenGL.GLUT import glutKeyboardFunc, glutKeyboardUpFunc
from bui.backend.event import BaseEventManager
from timer import Timer

class EventManager(BaseEventManager):
    def __init__(self, root_layout, hotkeys, events):
        super(EventManager, self).__init__(root_layout, hotkeys, events)
        
        glutKeyboardFunc(self.key_pressed)
        glutKeyboardUpFunc(self.key_released)
    
    def key_pressed(self, key, x, y):
        self.key_event(ord(key), pressed=True)
    
    def key_released(self, key, x, y):
        self.key_event(ord(key), pressed=False)
