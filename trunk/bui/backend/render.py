# -*- coding: utf-8 -*-
import sys
from bui.graphics.opengl.draw import draw_rectangle
from bui.utils.attribute import set_attributes_based_on_kvargs
from bui.utils.coordinate import Coordinate
from bui.utils.math import clamp
from bui.utils.node import Node

# set width/height to auto if value is zero? else auto is false?
# TODO: figure out how to solve invert_y (to lower level?)
# TODO: abstract width/height?

class RenderNode(Node):
    def __init__(self, **kvargs):
        super(RenderNode, self).__init__()
        
        # TODO: convert bg_color to just bg (container) that can contain color/gradient/texture/etc. ?
        self.bg_color = None 
        
        self._visible = True
        
        self.x = 0
        self.y = 0
        
        self.auto_width = False
        self._width = 0
        self._min_width = 0
        self._max_width = sys.maxint
        
        self.auto_height = False
        self._height = 0
        self._min_height = 0 # TODO
        self._max_height = sys.maxint # TODO
        
        set_attributes_based_on_kvargs(self, **kvargs) # TEST!!! esp. children reference is important
    
    def append(self, item):
        self.children.append(item)
    
    def remove(self, item):
        self.children.remove(item)
    
    def get_parent(self):
        if hasattr(self, 'parents') and len(self.parents) > 0:
            return self.parents[0]
    parent = property(get_parent)
    
    def get_min_height(self):
        return self._min_height
    def set_min_height(self, min_height):
        self._min_height = min_height
    min_height = property(get_min_height, set_min_height)
    
    def get_max_height(self):
        return self._max_height
    def set_max_height(self, max_height):
        self._max_height = max_height
    max_height = property(get_max_height, set_max_height)
    
    def get_height(self):
        print 'get height'
        # XXX: this gets stuck in recursion in simple.py
        
        if self._height:
            return self._height
        
        element_height = self.find_element_height()
        
        if element_height:
            return element_height
        
        return 0
    def set_height(self, height):
        self._height = max(height, 0)
    height = property(get_height, set_height)
    
    # XXX: rewrite to use children etc.
    def find_element_height(self):
        parent = self.parent
        
        if not parent:
            return None
        
        if hasattr(parent, 'element_height') and parent.element_height:
            return parent.element_height
        
        return parent.find_element_height()
    
    def get_min_width(self):
        return self._min_width
    def set_min_width(self, min_width):
        self._min_width = max(min(min_width, self.max_width), 0)
    min_width = property(get_min_width, set_min_width)
    
    def get_max_width(self):
        if self.parent:
            from layout import FreeLayout # FIXME: hack to solve cyclic dependency
            if self._max_width < self.parent.width or isinstance(self.parent, FreeLayout):
                return self._max_width
            return self.parent.width
        
        return sys.maxint
    def set_max_width(self, max_width):
        self._max_width = max(max_width, self.min_width)
    max_width = property(get_max_width, set_max_width)
    
    def get_width(self):
        print 'get width'
        
        width = 0
        
        if self.parent:
            # ok??? if width is zero use parent width?
            width = self._width if self._width else self.parent.width
            
            if self.auto_width:
                width = self.parent.width
        elif not self.auto_width:
            width = self._width
        
        return clamp(width, self.min_width, self.max_width)
    def set_width(self, width):
        if width == 'auto':
            self.auto_width = True
        
        self._width = width
    width = property(get_width, set_width)
    
    def get_visible(self):
        if self.find_parent(visible=False):
            return False
        
        return self._visible
    def set_visible(self, visible):
        self._visible = visible
    visible = property(get_visible, set_visible)
    
    def render(self, render_coordinate=None):
        if render_coordinate:
            render_coordinate.x += self.x
            render_coordinate.y += self.y
        else:
            render_coordinate = Coordinate(self.x, self.y)
        
        self.render_bg_color(render_coordinate)
        
        return render_coordinate
    
    def render_bg_color(self, render_coordinate):
        if self.bg_color:
            draw_rectangle(self.bg_color, render_coordinate.x, render_coordinate.y,
                           render_coordinate.x + self.width, render_coordinate.y + self.height)
