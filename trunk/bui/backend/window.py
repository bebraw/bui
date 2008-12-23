# -*- coding: utf-8 -*-
from bui.utils.coordinate import Coordinate

class BaseWindowManager(object):
    def get_coordinates(self):
        return (0, 0, 0, 0, )
    
    def get_initial_coordinates(self):
        return Coordinate(0, self.height)
    
    def get_height(self):
        xmin, ymin, xmax, ymax = self.get_coordinates()
        
        return ymax - ymin
    height = property(get_height)
    
    def get_width(self):
        xmin, ymin, xmax, ymax, = self.get_coordinates()
        
        return xmax - xmin
    width = property(get_width)
