# -*- coding: utf-8 -*-
from abstract import AbstractContainer

class EmptyContainer(AbstractContainer):
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

class VerticalContainer(AbstractContainer):
    def render(self, coord):
        for child in self.children:
            if child.visible:
                coord.y -= child.height
                child.render(coord)
