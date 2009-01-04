# -*- coding: utf-8 -*-
from __future__ import division
from OpenGL.GLUT import glutTimerFunc
from bui.backend.timer import BaseTimer, BaseTimerManager

class TimerManager(BaseTimerManager):
    def __init__(self, window, timers):
        if timers:
            for timer_name in vars(timers).keys():
                if timer_name[0] != '_': # parse interval from __doc__
                    timer_func = getattr(timers, timer_name)
                    
                    # XXX: similar code as in constraint -> unify
                    doc_str = timer_func.__doc__.strip()
                    
                    try:
                        exec(doc_str)
                    except:
                        interval = 0
                    
                    self[timer_name] = Timer(window, timer_func, interval)

class Timer(BaseTimer):
    def __init__(self, window, func, interval_in_seconds):
        super(Timer, self).__init__(window, func, interval_in_seconds)
    
    def start(self):
        self._update(0)
    
    def _update(self, value):
        self.func(self.window, self, None) # TODO: timers reference
        glutTimerFunc(self.interval_in_ms, self._update, 0)
    
    def stop(self):
        return NotImplemented
    
    def pause(self):
        return NotImplemented
    
    def resume(self):
        return NotImplemented
