# -*- coding: utf-8 -*-
from abstract import AbstractContainer

class Fill(AbstractContainer):
    def render(self, coord):
        pass

class HorizontalContainer(AbstractContainer):
    def render(self, coord):
        tmp_x = coord.x
        
        for child in self.children:
            if child.visible:
                child.render(coord)
                coord.x += child.width
        
        coord.x = tmp_x
    
    def find_child_max_height(self): # TODO: test!
        record_height = 0
        
        for child in self.children:
            record_height = max(record_height, child.height)
        
        return record_height

class VerticalContainer(AbstractContainer):
    def render(self, coord):
        coord.x += self.x_offset
        coord.y += self.y_offset
        
        for child in self.children:
            if child.visible:
                child.render(coord)
                coord.y -= child.height
