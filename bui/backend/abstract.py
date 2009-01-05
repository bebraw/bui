# -*- coding: utf-8 -*-
import sys
from bui.graphics.opengl.draw import draw_rectangle
from bui.utils.coordinate import Coordinate
from bui.utils.math import clamp
from bui.utils.tree import TreeChild, TreeParent

# TODO: figure out how to solve invert_y (to lower level?)
# should it be possible to access sibling of window???
# TODO: rethink the property based system (minimize amount of calculation needed
# by using listener based setup?

class AbstractObject(TreeChild):
    def __init__(self, **kvargs):
        super(AbstractObject, self).__init__(**kvargs)
        
        self.name = ''
        self.tooltip = ''
        
        # TODO: convert bg_color to just bg (container) that can contain color/gradient/texture/etc. ?
        self.bg_color = None 
        self._visible = True
        
        self.x = 0
        self.y = 0
        
        self.auto_width = False
        self._width = 0
        self._min_width = 0
        self._max_width = sys.maxint
        
        self._height = None
        # self.min_width = 0 # TODO
        # self.max_width = sys.maxint # TODO
        
        # TODO: check if this should be here! -> to event stuff???
        self.events = []
        self.event_index = 0
        
        # adapted from http://blog.enterthefoo.com/2008/08/pythons-vars.html
        for name in ( n for n in dir(self) if n[0] != '_' ):
            attr = getattr(self, name)
            
            # TODO: get rid of callable?
            if not callable(attr) and name in kvargs:
                if name is not 'children':
                    setattr(self, name, kvargs[name])
    
    def initialize_attributes(self):
        self.height = self.height
        self.width = self.width
    
    # TODO: should there be min and max height just like for width???
    
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
        self._height = max(height, 0) or None
    height = property(get_height, set_height)
    
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

class AbstractLayout(TreeParent, AbstractObject):
    def __init__(self, **kvargs):
        #super(TreeParent, self).__init__()
        self._element_height = None
        super(AbstractLayout, self).__init__(**kvargs)
    
    def get_element_height(self):
        if self.parent:
            return min(self.parent.height, self._element_height)
        
        return min(self._height, self._element_height)
    def set_element_height(self, element_height):
        self._element_height = element_height
    element_height = property(get_element_height, set_element_height)
    
    def render_child(self, child, render_coordinate):
        if child.visible:
            if isinstance(child, AbstractLayout):
                render_coordinate = child.render(render_coordinate)
            else:
                child.x = render_coordinate.x
                child.y = render_coordinate.y
                child.render_bg_color(render_coordinate)
                child.render()
        
        return render_coordinate
    
    def append(self, abstract_object):
        super(AbstractLayout, self).append(abstract_object)
        
        # XXX: set up observers
        # get rid of this? how to update events?
        #if hasattr(self.common, 'application'):
        #    self.common.application.update_structure()
    
    def remove(self, abstract_object):
        super(AbstractLayout, self).remove(abstract_object)
        
        # XXX: set up observers
        # get rid of this? how to update events?
        #if hasattr(self.common, 'application'):
        #    self.common.application.update_structure()
