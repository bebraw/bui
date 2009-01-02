# -*- coding: utf-8 -*-
from OpenGL.GLUT import glutTimerFunc

# TODO: add start and stop too!
class Timer():
    def __init__(self, root_elem, func, interval_in_seconds):
        self.root_elem = root_elem
        self.func = func
        self.interval_in_seconds = interval_in_seconds
        
        self._update(0)
    
    def _update(self, value):
        self.func(self.root_elem, self)
        glutTimerFunc(self.interval_in_ms, self._update, 0)
    
    def get_interval_in_ms(self):
        return int(self.interval_in_seconds * 1000)
    interval_in_ms = property(get_interval_in_ms)
    
    def get_interval_in_seconds(self):
        if hasattr(self, '_interval_in_seconds'):
            return self._interval_in_seconds
    def set_interval_in_seconds(self, interval_in_seconds):
        self._interval_in_seconds = max(0.001, interval_in_seconds)
    interval_in_seconds = property(get_interval_in_seconds, set_interval_in_seconds)
