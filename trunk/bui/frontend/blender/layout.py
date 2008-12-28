# -*- coding: utf-8 -*-
from bui.utils.coordinate import Coordinate

from bui.backend.abstract import AbstractContainer
from bui.backend.layout import BaseLayoutManager

class LayoutManager(BaseLayoutManager):
    def initialize_coordinates(self, coord=None):
        def initialize_coordinates_recursion(elem):
            if elem.x is not None:
                elem.x = int(elem.x)
            
            if elem.y is not None:
                elem.y = 2 * self.window_manager.height - elem.y - elem.height
                elem.y = int(elem.y)
            
            elem.height = int(elem.height)
            elem.width = int(elem.width)
            
            if isinstance(elem, AbstractContainer):
                for child in elem.children:
                    initialize_coordinates_recursion(child)
        
        coord = Coordinate(0, self.window_manager.height)
        
        super(LayoutManager, self).initialize_coordinates(coord)
        
        initialize_coordinates_recursion(self.root_container)
