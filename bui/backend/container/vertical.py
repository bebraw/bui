# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject
from abstract import AbstractContainer

class VerticalContainer(AbstractContainer):
    def get_height(self):
        if self.visible:
            # TODO: make it possible to determine height explicitly (-> scrollbar)
            self._height = 0
            
            heights = []
            for child in self.children:
                if child.visible and child.height:
                    heights.append(child.height)
            
            self._height = sum(heights)
        
        return super(AbstractContainer, self).get_height()
    height = property(get_height, AbstractObject.set_height)
    
    def render(self):
        super(VerticalContainer, self).render()
        
        for child in self.children:
            if child.visible:
                child.render()
            
            if not isinstance(child, VerticalContainer):
                self.common.render_coordinate.y += child.height
