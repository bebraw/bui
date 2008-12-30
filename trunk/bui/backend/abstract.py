# -*- coding: utf-8 -*-
from bui.utils.math import clamp
from bui.utils.singleton import Singleton
from bui.utils.tree import TreeChild, TreeParent

class AbstractObject(object):
    def __init__(self, **kvargs):
        super(AbstractObject, self).__init__(**kvargs)
        
        self.x_offset = 0
        self.y_offset = 0
        self.name = ''
        
        self.height = 0
        
        # TODO: make auto_width hidden (to AbstractChild) and use width = 'auto' instead?
        self.auto_width = False
        self.min_width = 0
        self.max_width = 0
        self.width = None
        
        self.event_handler = None
        self.visible = True
        self.bg_color = None
        self.events = []
        
        # should make this hidden! (make it possible not to override this via serializer)
        self.common = Singleton()
        
        # default attribute values for common
        if not hasattr(self.common, 'element_height'):
            self.common.element_height = 20
        
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
        return self._width
    def set_width(self, width):
        if self.auto_width:
            self._width = clamp(width, self.min_width, self.max_width)
        else:
            self._width = max(width, 0)
    width = property(get_width, set_width)
    
    def get_visible(self):
        return self._visible
    def set_visible(self, visible):
        self._visible = visible
    visible = property(get_visible, set_visible)
    
    def render(self):
        pass
    
    def render_bg_color(self):
        pass

class AbstractChild(TreeChild, AbstractObject):
    def __init__(self, **kvargs):
        super(AbstractChild, self).__init__(**kvargs)
    
    # move whole property here?
    def get_visible(self):
        hidden_parent = self.find_parent(visible=False)
        
        if hidden_parent:
            return False
        
        return self._visible
    visible = property(get_visible, AbstractObject.set_visible)
