# -*- coding: utf-8 -*-
import sys

class ConstraintManager(object):
    def __init__(self, root_container, namespace):
        self.root_container = root_container
        
        self.initialize_constraint_list(namespace)
        #self.check_constraints() # TODO! should be called explicitly?
    
    def initialize_constraint_list(self, namespace):
        self.constraints = ConstraintContainer()
        
        for func_name in namespace.keys():
            if func_name.endswith('_constraint'):
                self.constraints.append(namespace[func_name])
    
    def check_constraints(self):
        for constraint in self.constraints: # implement __iter__ for this!
            constraint(self.root_container)

class ConstraintContainer(object):
    def __init__(self):
        self.constraints = {}
    
    def __getitem__(self, item):
        i = 0
        
        for priority, funcs in self.constraints.iteritems():
            for func in funcs:
                if i == item:
                    return func
                
                i += 1
    
    def __len__(self):
        total_len = 0
        
        for priority, funcs in self.constraints.iteritems():
            total_len += len(funcs)
        
        return total_len
    
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
