# -*- coding: utf-8 -*-
from bui.utils.tree import TreeChild, TreeParent

class AbstractObject(object):
    def __init__(self, **kvargs):
        self.x_offset = 0
        self.y_offset = 0
        self.name = ''
        self.height = None
        self.width = None
        self.event_handler = None
        self.visible = True
        self.bg_color = None
        self.events = []
        super(AbstractObject, self).__init__(**kvargs)
        
        for suitable_value in self.__dict__:
            arg_value = self.__check_arg(kvargs, suitable_value)
            
            if arg_value is not None:
                self.__dict__[suitable_value] = arg_value
    
    def __check_arg(self, dict, arg):
        if dict.has_key(arg):
            return dict[arg]
    
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
