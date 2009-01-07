# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject

class Element(AbstractObject):
    def __init__(self, **kvargs):
        self.tooltip = ''
        super(Element, self).__init__(**kvargs)

class Fill(Element):
    pass
