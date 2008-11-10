# -*- coding: utf-8 -*-
from serializer import unserialize

class TreeChild(object):
    def __init__(self, args=None):
        super(TreeChild, self).__init__(args)
        self.parent = None # should generalize this to parents later?
    
    def find_parent(self, name):
        parent = self.parent
        
        if not parent:
            return None
        
        if parent.name == name:
            return parent
        
        return parent.find_parent(name)
    
    def find_root_element(self):
        def find_root_element_recursion(elem):
            parent = elem.parent
            
            if not parent:
                return elem
            
            return find_root_element_recursion(parent)
        
        return find_root_element_recursion(self)
    
    #def find_element(self, name):
    #    pass # should try to find elem with given name. in this case can use only parent info
        # note that TreeParent should implement this too (knows only children). how to sync these behaviors?
        # should this be actually an external func?

class TreeParent(object):
    def __init__(self, args=None):
        super(TreeParent, self).__init__(args)
        self.children = []
    
    # this should be most likely separated from TreeParent as it deals with parent!
    def add_child_structure(self, structure, namespace):
        root_elem = self.find_root_element() # probably belongs outside this func
        
        structure_root = unserialize(structure, namespace)
        structure_root.parent = self
        structure_root.height = root_elem.height
        structure_root.initialize_element_heights(20) # FIXME: REALLY EVIL HACK! probably belongs outside this func
        structure_root.initialize_element_widths(root_elem.width) # probably belongs outside this func
        self.children.append(structure_root)
        
        return structure_root
    
    def _child_recursion(self, func, arg=None):
        for child in self.children:
            ret = func(child, self, arg)
            
            if ret:
                return ret
            
            if isinstance(child, TreeParent):
                child_ret = child._child_recursion(func, arg)
                
                if child_ret:
                    return child_ret
    
    def find_child(self, name=None, variable=None):
        def match_child_name(child, elem, name):
            if hasattr(child, 'name'):
                if child.name == name:
                    return child
        
        def match_child_variable(child, elem, var):
            if hasattr(child, 'variable'):
                if child.variable == var:
                    return child
        
        if name:
            return self._child_recursion(match_child_name, name)
        
        if variable:
            return self._child_recursion(match_child_variable, variable)
