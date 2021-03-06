# -*- coding: utf-8 -*-
import sys
from layout import Layout

class BaseConstraintManager(object):
    def __init__(self, root_layout, constraints):
        assert isinstance(root_layout, Layout)
        
        self.root_layout = root_layout
        
        self.initialize_constraint_list(constraints)
    
    def initialize_constraint_list(self, constraints):
        self.constraints = ConstraintContainer()
        
        for func_name in dir(constraints):
            if func_name.endswith('_constraint'):
                constraint = getattr(constraints, func_name)
                self.constraints.append(constraint)
    
    def check_constraints(self):
        for constraint in self.constraints:
            constraint(self.root_layout)

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
    
    def append(self, func):
        priority = self.get_priority(func)
        
        if priority in self.constraints:
            self.constraints[priority].append(func)
        else:
            self.constraints[priority] = [func, ]
    
    def get_priority(self, func):
        if func.__doc__:
            doc_str = func.__doc__.strip()
            try:
                exec(doc_str)
                
                if type(priority) is int and priority > 0:
                    return priority
            except:
                pass
        
        return sys.maxint
