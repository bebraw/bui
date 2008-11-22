# -*- coding: utf-8 -*-

class WindowManager(object):
    def __init__(self):
        self.x = 0
        self.y = self.get_window_height()

    def _get_window_coords(self):
        return (0, 0, 0, 0, )
    
    def get_window_height(self):
        xmin, ymin, xmax, ymax = self._get_window_coords()
        
        return ymax - ymin
    
    def get_window_width(self):
        xmin, ymin, xmax, ymax, = self._get_window_coords()
        
        return xmax - xmin
