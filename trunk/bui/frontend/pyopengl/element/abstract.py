# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject

class AbstractOpenGLElement(AbstractObject):
    def initialize(self, **kvargs):
        self.tooltip = ''
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        super(AbstractOpenGLElement, self).initialize(**kvargs)
