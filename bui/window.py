# -*- coding: utf-8 -*-
from coordinate import Coordinate
from layout import BaseLayoutManager

class BaseWindowManager(object):
    def __init__(self, root_container, element_height):
        self.layout_manager = BaseLayoutManager(root_container, element_height)
    
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
    
    def initialize_layout(self):
        coord = Coordinate(0, self.height)
        self.layout_manager.initialize_layout(coord)
