# -*- coding: utf-8 -*-
import sys
from bui.utils.coordinate import Coordinate
from bui.utils.math import clamp
from bui.utils.singleton import Singleton
from bui.utils.tree import TreeChild, TreeParent
from window import BaseWindowManager

class AbstractObject(TreeChild):
    def __init__(self):
        super(AbstractObject, self).__init__()
        self.common = Common()
        
        self.x = 0
        self.x_is_relative = True
        
        self.y = 0
        self.y_is_relative = True
    
    def initialize(self, **kvargs):
        self.name = ''
        
        self.height = 0
        
        self.width = None
        self.min_width = 0
        self.max_width = sys.maxint
        
        self.x_offset = 0
        self.y_offset = 0
        
        self.event_handler = None
        self.events = []
        self.variable = None
        
        self.visible = True
        self.bg_color = None
        
        # adapted from http://blog.enterthefoo.com/2008/08/pythons-vars.html
        for name in ( n for n in dir(self) if n[0] != '_' ):
            attr = getattr(self, name)
            
            if not callable(attr) and kvargs.has_key(name):
                setattr(self, name, kvargs[name])
    
    def get_height(self):
        if self.visible:
            if self._height is not None:
                return self._height
            return self.common.element_height
        return 0
    def set_height(self, height):
        self._height = max(height, 0) or None
    height = property(get_height, set_height)
    
    def get_min_width(self):
        if hasattr(self, '_min_width'):
            return self._min_width
        return 0
    def set_min_width(self, min_width):
        self._min_width = max(min(min_width, self.max_width), 0)
    min_width = property(get_min_width, set_min_width)
    
    def get_max_width(self):
        parent_width = sys.maxint
        ret_width = sys.maxint
        
        if hasattr(self.parent, 'width'):
            parent_width = self.parent.width
            ret_width = parent_width
        
        if hasattr(self, '_max_width'):
            if self._max_width < parent_width:
                ret_width = self._max_width
        
        return ret_width
    def set_max_width(self, max_width):
        self._max_width = max(max_width, self.min_width)
    max_width = property(get_max_width, set_max_width)
    
    def get_width(self):
        width = 0
        
        if hasattr(self, '_width'):
            if self.parent:
                width = self._width if self._width else self.parent.width
                
                if self._width == 'auto':
                    width = self.parent.width
            elif self.common.window_manager:
                width = self.common.window_manager.width
            elif self._width != 'auto':
                width = self._width
        
        return clamp(width, self.min_width, self.max_width)
    def set_width(self, width):
        self._width = width
    width = property(get_width, set_width)
    
    def get_visible(self):
        if self.find_parent(visible=False):
            return False
        
        return self._visible
    def set_visible(self, visible):
        self._visible = visible
    visible = property(get_visible, set_visible)
    
    def get_y(self):
        if self.common.invert_y and self.common.window_manager:
            return self.common.window_manager.height - self._y - self.height
        return self._y
    def set_y(self, y):
        self._y = y
    y = property(get_y, set_y)
    
    def initialize_render(self):
        self.common.render_coordinate = Coordinate()
    
    def render(self):
        if self.x_is_relative:
            self.x = self.common.render_coordinate.x
        
        if self.y_is_relative:
            self.y = self.common.render_coordinate.y
        
        self.common.render_coordinate.x += self.x_offset
        self.common.render_coordinate.y += self.y_offset
        
        self.render_bg_color()
    
    def render_bg_color(self):
        pass

class Common(Singleton):
    def __init__(self):
        if not hasattr(self, 'init_called'):
            self.init_called = True
            
            self.element_height = 20
            self.render_coordinate = Coordinate()
            self.invert_y = False
            self.window_manager = None
