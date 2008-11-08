# -*- coding: utf-8 -*-
from bui.parser import parse_structure

'''
TODO:
-TreeHelper needs to see all containers and elements! check Applications for this!
-add find_element (searches for root, then checks all children)
'''

class TreeHelper(object):
    def __init__(self, namespace, args=None):
        super(TreeHelper, self).__init__(namespace, args)
        self.children = []
        
        if type(args) is dict and args.has_key('children'):
            for child in args['children']:
                class_name = child.keys()[0]
                class_args = child.values()[0]
                
                if class_name == 'UIStructure':
                    structure_name = class_args['name']
                    ui_structure = namespace[structure_name]
                    class_instance = parse_structure(ui_structure, namespace)
                else:
                    class_instance = namespace[class_name](namespace, args=class_args)
                
                class_instance.parent = self
                self.children.append(class_instance)
    
    def add_child_structure(self, structure, after):
        elem_index = self._find_index_of_last_child(name=after)
        structure_root = parse_structure(structure)
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
    
    def _child_recursion(self, func, arg=None):
        for child in self.children:
            ret = func(child, self, arg)
            
            if ret:
                return ret
            
            child_ret = child._child_recursion(func, arg)
            
            if child_ret:
                return child_ret
    
    def find_child(self, name=None, variable=None):
        def match_child_name(child, elem, name):
            if child.name == name:
                return child
        
        def match_child_variable(child, elem, var):
            if child.variable == var:
                return child
        
        if name:
            return self._child_recursion(match_child_name, name)
        
        if variable:
            return self._child_recursion(match_child_variable, variable)
