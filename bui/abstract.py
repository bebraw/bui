# -*- coding: utf-8 -*-
from tree import TreeChild

class AbstractObject(object):
    def __init__(self, args=None): # TODO: convert to **kvargs?
        self.name = ''
        self.height = None
        self.width = None
        self.visible = True
        super(AbstractObject, self).__init__(args)
        
        if type(args) is dict:
            for suitable_value in self.__dict__:
                arg_value = self._check_arg(args, suitable_value)
                
                if arg_value is not None:
                    self.__dict__[suitable_value] = arg_value
    
    def _check_arg(self, dict, arg):
        if dict.has_key(arg):
            return dict[arg]

class AbstractAttributes(object):
    def __init__(self, args=None):
        self.event_handler = None
        self.visible = True
        super(AbstractAttributes, self).__init__(args)

class AbstractElement(TreeChild, AbstractAttributes, AbstractObject):
    def __init__(self, args=None):
        self.children = []
        self.variable = None
        super(AbstractElement, self).__init__(args)
