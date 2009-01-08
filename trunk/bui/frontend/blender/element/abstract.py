# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractNode

class AbstractBlenderElement(AbstractNode):
    def update_value(self, evt, val):
        self.value = val
