# -*- coding: utf-8 -*-
from OpenGL.GLUT import glutKeyboardFunc, glutKeyboardUpFunc, glutTimerFunc
from bui.backend.event import BaseEventManager

class EventManager(BaseEventManager):
    def __init__(self, root_elem, keys, events):
        super(EventManager, self).__init__(root_elem, keys, events)
        
        glutKeyboardFunc(self.key_pressed)
        glutKeyboardUpFunc(self.key_released)
        
        self.timer_func = None # just a hack to store one timer func. should make this more dynamic
        self.timers = TimersContainer()
    
    def key_pressed(self, key, x, y):
        print key, x, y
        self.key_event(key, pressed=True)
    
    def key_released(self, key, x, y):
        self.key_event(key, pressed=False)
    
    # should go elsewhere?
    def create_timer(self, func, interval):
        ''' interval in seconds! '''
        self.timers.append(Timer(self.root_elem, func, interval))

class TimersContainer(list):
    def update(self):
        for timer in self:
            timer.update()

# TODO: add start and stop too!
class Timer():
    def __init__(self, root_elem, func, interval_in_seconds):
        self.root_elem = root_elem
        self.begin_time = None
        self.func = func
        self.interval_in_seconds = interval_in_seconds
        
        self.running = True
        
        if self.running:
            self.func(self.root_elem)
            glutTimerFunc(self.interval_in_ms, self._update, 0)
    
    def _update(self, value):
        self.func(self.root_elem)
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
