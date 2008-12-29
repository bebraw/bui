# -*- coding: utf-8 -*-

class TreeChild(object):
    def __init__(self, **kvargs):
        super(TreeChild, self).__init__(**kvargs)
        self.parent = kvargs['parent'] if kvargs.has_key('parent') else None
    
    def _parent_recursion(self, variable_name, variable_value):
        try:
            variable_index = dir(self.parent).index(variable_name)
            variable = getattr(self.parent, dir(self.parent)[variable_index])
        except:
            variable = None
        
        if variable is not None:
            if variable == variable_value:
                return self.parent
            
            return self.parent._parent_recursion(variable_name, variable_value)
    
    def find_parent(self, **kvargs):
        if len(kvargs) == 1:
            arg_key = kvargs.keys()[0]
            arg_value = kvargs.values()[0]
            return self._parent_recursion(arg_key, arg_value)
    
    def find_root_element(self):
        parent = self.parent
        
        if not parent:
            return self
        
        return self.parent.find_root_element()

class TreeParent(object):
    def __init__(self, **kvargs):
        super(TreeParent, self).__init__(**kvargs)
        self.children = []
    
    def _child_recursion(self, variable_name, variable_value):
        if self.children:
            for child in self.children:
                if child and child.__dict__.has_key(variable_name):
                    if child.__dict__[variable_name] == variable_value:
                        return child
                
                if isinstance(child, TreeParent):
                    ret = child._child_recursion(variable_name, variable_value)
                    
                    if ret:
                        return ret
    
    def find_child(self, **kvargs):
        if len(kvargs) == 1:
            arg_key = kvargs.keys()[0]
            arg_value = kvargs.values()[0]
            return self._child_recursion(arg_key, arg_value)
    
    # TODO: override del instance.children instead? TEST!
    def remove_children(self):
        for child in self.children:
            child.parent = None
        
        self.children = []
