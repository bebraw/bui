# -*- coding: utf-8 -*-
from abstract import AbstractObject
from tree import TreeChild

class AbstractElement(TreeChild, AbstractObject):
    def __init__(self, args=None):
        self.children = []
        super(AbstractElement, self).__init__(args)

class EmptyElement(AbstractElement): 
    def render(self, coord):
        pass
