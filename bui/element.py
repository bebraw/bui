# -*- coding: utf-8 -*-
from abstract import AbstractObject
from treehelper import TreeHelper

class AbstractElement(AbstractObject, TreeHelper):
    suitable_values = ('width', )

class EmptyElement(AbstractElement): 
    def render(self, coord):
        pass
