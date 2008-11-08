# -*- coding: utf-8 -*-
import sys

from bui.constraint import ConstraintContainer, ConstraintManager

# IMPORTANT! Note that test names should not end with _constraint as
# this messes up with the constraint naming convention which we are
# testing here!

# TODO: check_constraints! also validation of root_container!

def priority_is_zero_constraint(root_elem):
    '''priority=0'''
    pass

def priority_is_one_constraint(root_elem):
    '''priority=1'''
    pass

def priority_is_two_constraint(root_elem):
    '''priority=2'''
    pass

def priority_is_two_too_constraint(root_elem):
    '''priority=2'''
    pass

def priority_is_negative_constraint(root_elem):
    '''priority=-3'''
    pass

def priority_is_not_int_constraint(root_elem):
    '''priority=cat'''
    pass

def some_constraint(root_elem):
    pass # could assert that root_elem is really root_elem

class TestConstraintManager():
    def setup_class(self):
        self.constraint_manager = ConstraintManager(root_container=None, namespace=globals())
    
    def test_initialize_constraint_list(self):
        self.constraint_manager.initialize_constraint_list(globals())
        
        assert len(self.constraint_manager.constraints) == 7
    
    def test_constraints_in_right_order_in_constraint_list(self):
        self.constraint_manager.initialize_constraint_list(globals())
        
        assert hasattr(self.constraint_manager, 'constraints')
        assert len(self.constraint_manager.constraints) == 7
        assert self.constraint_manager.constraints[0] == priority_is_one_constraint

class TestConstraintContainer():
    def setup_method(self, method):
        self.constraint_container = ConstraintContainer()
    
    def test_get_function_priority(self):
        get_priority = self.constraint_container._get_priority
        
        assert get_priority(some_constraint) == sys.maxint
        assert get_priority(priority_is_one_constraint) == 1
        assert get_priority(priority_is_two_constraint) == 2
        assert get_priority(priority_is_zero_constraint) == sys.maxint
        assert get_priority(priority_is_negative_constraint) == sys.maxint
        assert get_priority(priority_is_not_int_constraint) == sys.maxint
    
    def test_append(self):
        self.constraint_container.append(some_constraint)
        
        assert len(self.constraint_container) == 1
        assert self.constraint_container[0] == some_constraint
    
    def test_append_invalid(self):
        def not_valid():
            pass
        
        self.constraint_container.append(not_valid)
        
        assert len(self.constraint_container.constraints) == 1
        assert self.constraint_container[0] == not_valid
    
    def test_append_with_priority(self):
        self.constraint_container.append(priority_is_two_constraint)
        self.constraint_container.append(some_constraint)
        self.constraint_container.append(priority_is_one_constraint)
        
        assert len(self.constraint_container) == 3
        assert self.constraint_container[0] == priority_is_one_constraint
        assert self.constraint_container[1] == priority_is_two_constraint
        assert self.constraint_container[2] == some_constraint
    
    def test_append_with_same_priority(self):
        self.constraint_container.append(priority_is_two_constraint)
        self.constraint_container.append(priority_is_two_too_constraint)
        
        assert len(self.constraint_container) == 2
        assert self.constraint_container[0] == priority_is_two_constraint
        assert self.constraint_container[1] == priority_is_two_too_constraint
    
    def test_append_with_negative_priority(self):
        self.constraint_container.append(priority_is_two_constraint)
        self.constraint_container.append(priority_is_negative_constraint)
        
        assert len(self.constraint_container) == 2
        assert self.constraint_container[0] == priority_is_two_constraint
        assert self.constraint_container[1] == priority_is_negative_constraint
