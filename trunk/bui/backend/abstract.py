# -*- coding: utf-8 -*-
from bui.utils.coordinate import Coordinate
from bui.utils.math import clamp
from bui.utils.singleton import Singleton
from bui.utils.tree import TreeChild, TreeParent

class AbstractObject(TreeChild):
    def __init__(self):
        super(AbstractObject, self).__init__()
        self.common = Common()
        
        self.x = 0
        self.y = 0
    
    def initialize(self, **kvargs):
        self.name = ''
        
        self.height = 0
        
        # TODO: make auto_width hidden (to AbstractChild) and use width = 'auto' instead?
        self.auto_width = False
        self.min_width = 0
        self.max_width = 0
        self.width = None
        
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
        return self._min_width
    def set_min_width(self, min_width):
        if hasattr(self, 'max_width'):
            tmp_width = min(min_width, self.max_width)
        else:
            tmp_width = min_width
        
        self._min_width = max(tmp_width, 0)
    min_width = property(get_min_width, set_min_width)
    
    def get_max_width(self):
        return self._max_width
    def set_max_width(self, max_width):
        if hasattr(self, 'min_width'):
            tmp_width = max(max_width, self.min_width)
        else:
            tmp_width = max_width
        
        self._max_width = max(tmp_width, 0)
    max_width = property(get_max_width, set_max_width)
    
    def get_width(self):
        if self.auto_width:
            return clamp(self._width, self.min_width, self.max_width)
        return self._width
    def set_width(self, width):
        self._width = max(width, 0)
    width = property(get_width, set_width)
    
    def get_visible(self):
        return self._visible
    def set_visible(self, visible):
        self._visible = visible
    visible = property(get_visible, set_visible)
    
    def get_y(self):
        if self.common.invert_y and hasattr(self.common, 'window_manager'):
            return self.common.window_manager.height - self._y - self.height
        return self._y
    def set_y(self, y):
        self._y = y
    y = property(get_y, set_y)
    
    def initialize_render(self):
        self.common.render_coordinate = Coordinate()
    
    def render(self):
        # TODO: how to handle absolute coords?
        self.x = self.common.render_coordinate.x # to property?
        self.y = self.common.render_coordinate.y # to property?
        
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
