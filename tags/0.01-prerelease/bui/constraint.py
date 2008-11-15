# -*- coding: utf-8 -*-
import sys

class ConstraintManager(object):
    def __init__(self, root_container, namespace):
        self.root_container = root_container
        
        self.initialize_constraint_list(namespace)
    
    def initialize_constraint_list(self, namespace):
        self.constraints = ConstraintContainer()
        
        for func_name in namespace.keys():
            if func_name.endswith('_constraint'):
                self.constraints.append(namespace[func_name])
    
    def check_constraints(self):
        for constraint in self.constraints:
            constraint(self.root_container)

class ConstraintContainer(object):
    def __init__(self):
        self.constraints = {}
    
    def __getitem__(self, item):
        for i, func in enumerate(self):
            if i == item:
                return func
    
    def __len__(self):
        total_len = 0
        
        for func in self:
            total_len += 1
        
        return total_len
    
    def __iter__(self):
        for funcs in self.constraints.values():
            for func in funcs:
                yield func
    
    def _get_priority(self, func):
        doc_str = func.__doc__
        
        if doc_str:
            try:
                exec(doc_str)
                
                if type(priority) is int and priority > 0:
                    return priority
            except:
                pass
        
        return sys.maxint
    
    def append(self, func):
        priority = self._get_priority(func)
        
        if self.constraints.has_key(priority):
            self.constraints[priority].append(func)
        else:
            self.constraints[priority] = [func, ]
