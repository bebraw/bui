# -*- coding: utf-8 -*-
from bui.abstract import AbstractContainer
from bui.layout import BaseLayoutManager

class LayoutManager(BaseLayoutManager):
    def initialize_coordinates(self, coord):
        def initialize_coordinates_recursion(elem):
            elem.y = elem.y - elem.height
            
            elem.x = int(elem.x)
            elem.y = int(elem.y)
            elem.height = int(elem.height)
            elem.width = int(elem.width)
            
            if isinstance(elem, AbstractContainer):
                for child in elem.children:
                    initialize_coordinates_recursion(child)
        
        super(LayoutManager, self).initialize_coordinates(coord)
        
        initialize_coordinates_recursion(self.root_container)
