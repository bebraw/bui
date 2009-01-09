# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractNode

class Element(AbstractNode):
    def __init__(self, **kvargs):
        self.tooltip = ''
        super(Element, self).__init__(**kvargs)

class Fill(Element):
    pass
