# -*- coding: utf-8 -*-
from tree import TreeChild, TreeParent

class AbstractObject(object):
    def __init__(self, **kvargs):
        self.name = ''
        self.height = None
        self.width = None
        self.event_handler = None
        self.visible = True
        self.events = []
        super(AbstractObject, self).__init__(**kvargs)
        
        for suitable_value in self.__dict__:
            arg_value = self.__check_arg(kvargs, suitable_value)
            
            if arg_value is not None:
                self.__dict__[suitable_value] = arg_value
    
    def __check_arg(self, dict, arg):
        if dict.has_key(arg):
            return dict[arg]

class AbstractElement(TreeChild, AbstractObject):
    def __init__(self, **kvargs):
        self.children = []
        self.variable = None
        super(AbstractElement, self).__init__(**kvargs)

class AbstractContainer(TreeChild, TreeParent, AbstractObject):
    def __init__(self, **kvargs):
        self.x_offset = 0
        self.y_offset = 0
        super(AbstractContainer, self).__init__(**kvargs)
    
    def add_child_structure(self, structure_root):
        structure_root.parent = self
        self.children.append(structure_root)
    
    def has_only_container_children(self):
        if self.children:
            for child in self.children:
                if not isinstance(child, AbstractContainer):
                    return False
            
            return True
        
        return False
