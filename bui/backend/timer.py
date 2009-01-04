# -*- coding: utf-8 -*-

class BaseTimerManager(dict):
    def start(self):
        for timer in self.values():
            timer.start()
    
    def stop(self):
        for timer in self.values():
            timer.stop()
    
    def pause(self):
        for timer in self.values():
            timer.pause()
    
    def resume(self):
        for timer in self.values():
            timer.resume()

class BaseTimer(object):
    def __init__(self, window, func, interval_in_seconds):
        self.window = window
        self.func = func
        self.interval_in_seconds = interval_in_seconds
    
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def pause(self):
        pass
    
    def resume(self):
        pass
    
    def get_interval_in_ms(self):
        return int(self.interval_in_seconds * 1000)
    interval_in_ms = property(get_interval_in_ms)
    
    def get_interval_in_seconds(self):
        if hasattr(self, '_interval_in_seconds'):
            return self._interval_in_seconds
    def set_interval_in_seconds(self, interval_in_seconds):
        self._interval_in_seconds = max(0.001, interval_in_seconds)
    interval_in_seconds = property(get_interval_in_seconds, set_interval_in_seconds)
