# -*- coding: utf-8 -*-
from tree import TreeChild

class AbstractObject(object):
    suitable_values = ('event_handler', 'height', 'name', 'visible', 'width', )
    
    def __init__(self, args=None):
        self.name = ''
        self.visible = True
        super(AbstractObject, self).__init__(args)
        
        if type(args) is dict:
            for suitable_value in self.suitable_values:
                arg_value = self.check_arg(args, suitable_value)
                
                if arg_value is not None:
                    self.__dict__[suitable_value] = arg_value
    
    def check_arg(self, dict, arg):
        if dict.has_key(arg):
            return dict[arg]

class AbstractElement(TreeChild, AbstractObject):
    def __init__(self, args=None):
        self.children = []
        super(AbstractElement, self).__init__(args)
