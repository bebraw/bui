# -*- coding: utf-8 -*-
from abstract import AbstractContainer

class Fill(AbstractContainer):
    pass

class HorizontalContainer(AbstractContainer):
    def render(self, coord):
        super(HorizontalContainer, self).render(coord)
        
        tmp_x = coord.x
        
        for child in self.children:
            if child.visible:
                tmp_y = None
                
                if isinstance(child, VerticalContainer):
                    tmp_y = coord.y
                
                child.render(coord)
                coord.x += child.width
                
                coord.y = tmp_y or coord.y
        
        coord.x = tmp_x
    
    def find_child_max_height(self): # TODO: test!
        record_height = 0
        
        for child in self.children:
            record_height = max(record_height, child.height)
        
        return record_height

class VerticalContainer(AbstractContainer):
    def render(self, coord):
        super(VerticalContainer, self).render(coord)
        
        coord.x += self.x_offset
        coord.y += self.y_offset
        
        for child in self.children:
            if child.visible:
                child.render(coord)
                
                if not (isinstance(child, AbstractContainer) and
                        child.has_only_container_children()):
                    coord.y -= child.height
