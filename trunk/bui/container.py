# -*- coding: utf-8 -*-
from abstract import AbstractContainer

class Fill(AbstractContainer):
    pass

class HorizontalContainer(AbstractContainer):
    def find_child_max_height(self): # TODO: test!
        record_height = 0
        
        for child in self.children:
            record_height = max(record_height, child.height)
        
        return record_height

class VerticalContainer(AbstractContainer):
    pass
