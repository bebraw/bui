# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject

from abstract import AbstractContainer

class VerticalContainer(AbstractContainer):
    def get_height(self):
        if self.visible:
            # TODO: make it possible to determine height explicitly (-> scrollbar)
            self._height = 0
            
            if hasattr(self, 'children'):
                heights = []
                for child in self.children:
                    if child.visible and child.height:
                        heights.append(child.height)
                
                self._height = sum(heights)
        
        return super(AbstractContainer, self).get_height()
    height = property(get_height, AbstractObject.set_height)
    
    def set_width(self, width):
        self._width = max(width, 0)
        
        if hasattr(self, 'children'):
            for child in self.children:
                child.width = self.width
        
        super(AbstractContainer, self).set_width(width)
    width = property(AbstractContainer.get_width, set_width)
