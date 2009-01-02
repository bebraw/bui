# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject

class AbstractBlenderElement(AbstractObject):
    def update_value(self, evt, val):
        self.value = val
