# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractChild

class AbstractElement(AbstractChild):
    def __init__(self, **kvargs):
        self.children = [] # FIXME: get rid of this at some point
        self.variable = None # this belongs here?
        self.x = None # x and y belong here?
        self.y = None
        super(AbstractElement, self).__init__(**kvargs)
