# -*- coding: utf-8 -*-
import sys
from bui.graphics.opengl.draw import draw_rectangle
from bui.utils.attribute import set_attributes_based_on_kvargs
from bui.utils.coordinate import Coordinate
from bui.utils.node import Node
import value
from value import ConstrainedValue

# TODO: figure out how to solve invert_y (to lower level?)

protected_attributes = ('children', 'parents', )
class AbstractNode(Node):
    def __init__(self, **kvargs):
        super(AbstractNode, self).__init__()
        
        self.name = ''
        
        # TODO: check if this should be here! -> to event stuff???
        self.events = []
        self.event_index = 0
        
        # TODO: convert bg_color to just bg (container) that can contain color/gradient/texture/etc. ?
        self.bg_color = None 
        
        self._visible = True
        
        self.x = 0
        self.y = 0
        
        self._constrained_width = ConstrainedValue('width', self, value.ABSOLUTE, 0, 0, sys.maxint)
        self._constrained_height = ConstrainedValue('height', self, value.ABSOLUTE, 0, 0, sys.maxint)
        
        set_attributes_based_on_kvargs(self, excluded_attributes=protected_attributes, **kvargs)
        
        if 'width' not in kvargs:
            self._constrained_width.mode = value.AUTO
        
        if 'height' not in kvargs:
            self._constrained_height.mode = value.AUTO
    
    def get_width(self):
        return self._constrained_width.value
    def set_width(self, width):
        self._constrained_width.value = width
    width = property(get_width, set_width)
    
    def get_width_mode(self):
        return self._constrained_width.mode
    def set_width_mode(self, width_mode):
        self._constrained_width.mode = width_mode
    width_mode = property(get_width_mode, set_width_mode)
    
    def get_min_width(self):
        return self._constrained_width.min_value
    def set_min_width(self, min_width):
        self._constrained_width.min_value = min_width
    min_width = property(get_min_width, set_min_width)
    
    def get_max_width(self):
        return self._constrained_width.max_value
    def set_max_width(self, max_width):
        self._constrained_width.max_value = max_width
    max_width = property(get_max_width, set_max_width)
    
    def get_height(self):
        return self._constrained_height.value
    def set_height(self, height):
        self._constrained_height.value = height
    height = property(get_height, set_height)
    
    def get_height_mode(self):
        return self._constrained_height.mode
    def set_height_mode(self, height_mode):
        self._constrained_height.mode = height_mode
    height_mode = property(get_height_mode, set_height_mode)
    
    def get_min_height(self):
        return self._constrained_height.min_value
    def set_min_height(self, min_height):
        self._constrained_height.min_value = min_height
    min_height = property(get_min_height, set_min_height)
    
    def get_max_height(self):
        return self._constrained_height.max_value
    def set_max_height(self, max_height):
        self._constrained_height.max_value = max_height
    max_height = property(get_max_height, set_max_height)
    
    def get_parent(self):
        if hasattr(self, 'parents') and len(self.parents) > 0:
            return self.parents[0]
    parent = property(get_parent)
    
    def find_default_value(self, attribute_name):
        default_attribute_name = 'default_node_' + attribute_name
        
        parent = self.find_parent_with_attribute(default_attribute_name)
        
        if parent:
            return getattr(parent, default_attribute_name)
    
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
