# -*- coding: utf-8 -*-
from bui.utils.math import clamp
from bui.utils.tree import TreeChild, TreeParent

class AbstractObject(object):
    def __init__(self, **kvargs):
        super(AbstractObject, self).__init__(**kvargs)
        
        self.x_offset = 0
        self.y_offset = 0
        self.name = ''
        self.height = None
        
        self.auto_width = False
        self.min_width = 0
        self.max_width = 0
        self.width = None
        
        self.event_handler = None
        self.visible = True
        self.bg_color = None
        self.events = []
        
        # adapted from http://blog.enterthefoo.com/2008/08/pythons-vars.html
        for name in ( n for n in dir(self) if n[0] != '_' ):
            attr = getattr(self, name)
            
            if not callable(attr) and kvargs.has_key(name):
                setattr(self, name, kvargs[name])
    
    def get_height(self):
        if self.visible:
            return self._height
        
        return 0
    def set_height(self, height):
        self._height = max(height, 0)
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
    def get_visible(self):
        hidden_parent = self.find_parent(visible=False)
        
        if hidden_parent:
            return False
        
        return self._visible
    visible = property(get_visible, AbstractObject.set_visible)

class AbstractElement(AbstractChild):
    def __init__(self, **kvargs):
        self.children = [] # FIXME: get rid of this at some point
        self.variable = None # this belongs here?
        self.x = None # x and y belong here?
        self.y = None
        super(AbstractElement, self).__init__(**kvargs)

class AbstractContainer(TreeParent, AbstractChild):
    def append(self, abstract_object):
        abstract_object.parent = self
        self.children.append(abstract_object)
        
        self.update_structure()
    
    def remove(self, abstract_object):
        self.children.remove(abstract_object)
        
        self.update_structure()
    
    def render(self):
        self.render_bg_color()
        
        for child in self.children:
            if child.visible:
                child.render_bg_color()
                child.render()
    
    def update_structure(self):
        root_elem = self.find_root_element()
        
        if hasattr(root_elem, 'application'):
            root_elem.application.update_structure()
