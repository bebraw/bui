# -*- coding: utf-8 -*-
from bui.utils.tree import TreeChild, TreeParent

class AbstractObject(object):
    def __init__(self, **kvargs):
        super(AbstractObject, self).__init__(**kvargs)
        
        self.x_offset = 0
        self.y_offset = 0
        self.name = ''
        self.height = None
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
        return self._height
    def set_height(self, height):
        self._height = max(height, 0)
    height = property(get_height, set_height)
    
    def get_width(self):
        return self._width
    def set_width(self, width):
        self._width = max(width, 0)
    width = property(get_width, set_width)
    
    def render(self):
        pass
    
    def render_bg_color(self):
        pass

class AbstractElement(TreeChild, AbstractObject):
    def __init__(self, **kvargs):
        self.children = []
        self.variable = None
        super(AbstractElement, self).__init__(**kvargs)

class AbstractContainer(TreeChild, TreeParent, AbstractObject):
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
