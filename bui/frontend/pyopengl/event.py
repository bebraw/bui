# -*- coding: utf-8 -*-
from OpenGL.GLUT import glutKeyboardFunc, glutKeyboardUpFunc

from bui.backend.event import BaseEventManager

#from keys import PYOPENGL_KEYS

class EventManager(BaseEventManager):
    def __init__(self, root_container, keys, events):
        super(EventManager, self).__init__(root_container, keys, events)
        
        glutKeyboardFunc(self.key_pressed)
        glutKeyboardUpFunc(self.key_released)
    
    def key_pressed(self, key, x, y):
        self.key_event(key, pressed=True)
    
    def key_released(self, key, x, y):
        self.key_event(key, pressed=False)
    
#    def construct_key_event_ids(self, keys, key_mapping=None):
#        super(EventManager, self).construct_key_event_ids(keys, PYOPENGL_KEYS)
