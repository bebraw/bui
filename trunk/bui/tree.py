# -*- coding: utf-8 -*-

class TreeChild(object):
    def find_parent(self, name):
        parent = self.parent
        
        if not parent:
            return None
        
        if parent.name == name:
            return parent
        
        return parent.find_parent(name)
    
    def find_root_element(self, elem=None):
        parent = self.parent
        
        if elem:
            parent = elem.parent
        
        if not parent:
            return elem
        
        return self.find_root_element(parent)
    
    #def find_element(self, name):
    #    pass # should try to find elem with given name. in this case can use only parent info
        # note that TreeParent should implement this too (knows only children). how to sync these behaviors?
        # should this be actually an external func?

class TreeParent(object):
    def add_child_structure(self, structure, after):
        elem_index = self._find_index_of_last_child(name=after)
        structure_root = parse_structure(structure, self.namespace) # namespace is a bit problematic
        structure_root.parent = self
        self.children.insert(elem_index, structure_root)
        
        return structure_root
    
    def _find_index_of_last_child(self, name):
        found_layer = False
        last_layer = 0
        
        for i, child in enumerate(self.children):
            last_layer = i
            
            if child.name == name:
                found_layer = True
                last_layer += 1
            elif found_layer:
                break
        
        return last_layer
    
    def _child_recursion(self, func, arg=None):
        if hasattr(self, 'children'):
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
