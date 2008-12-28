# -*- coding: utf-8 -*-

class BaseWindowManager(object):
    def __init__(self, name=None, width=None, height=None):
        self.name = name
        self.width = width
        self.height = height
    
    def get_height(self):
        return self._height
    def set_height(self, height):
        self._height = max(height, 1)
    height = property(get_height, set_height)
    
    def get_width(self):
        return self._width
    def set_width(self, width):
        self._width = max(width, 1)
    width = property(get_width, set_width)
