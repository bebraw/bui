# -*- coding: utf-8 -*-
from treehelper import TreeHelper

'''
TODO:
-clean up abstract classes (suitable_values, __init__)
'''

class AbstractObject(object):
    suitable_values = None
    
    def __init__(self, namespace, args=None):
        self.visible = True # is this on right abstraction level?
        super(AbstractObject, self).__init__(namespace, args)
        
        if type(args) is dict:
            for suitable_value in self.suitable_values:
                arg_value = self.check_arg(args, suitable_value)
                
                if arg_value is not None:
                    self.__dict__[suitable_value] = arg_value
    
    def __getattr__(self, name):
        return None
    
    def check_arg(self, dict, arg):
        if dict.has_key(arg):
            return dict[arg]
