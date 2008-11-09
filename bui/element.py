# -*- coding: utf-8 -*-
from abstract import AbstractObject
from tree import TreeChild

class AbstractElement(TreeChild, AbstractObject):
    pass

class EmptyElement(AbstractElement): 
    def render(self, coord):
        pass
