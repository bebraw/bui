# -*- coding: utf-8 -*-

class BaseWindowManager(object):
    def __init__(self):
        self.x = 0
        self.y = self.height

    def get_coordinates(self):
        return (0, 0, 0, 0, )
    
    def get_height(self):
        xmin, ymin, xmax, ymax = self.get_coordinates()
        
        return ymax - ymin
    height = property(get_height)
    
    def get_width(self):
        xmin, ymin, xmax, ymax, = self.get_coordinates()
        
        return xmax - xmin
    width = property(get_width)
