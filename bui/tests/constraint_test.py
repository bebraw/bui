# -*- coding: utf-8 -*-
import sys

from bui.constraint import ConstraintContainer, BaseConstraintManager

root_container_name = 'test_container'

class Constraints():
    @staticmethod
    def priority_is_zero_constraint(root_elem):
        '''priority=0'''
        assert root_elem == root_container_name
    
    @staticmethod
    def priority_is_one_constraint(root_elem):
        '''priority=1'''
        assert root_elem == root_container_name
    
    @staticmethod
    def priority_is_two_constraint(root_elem):
        '''priority=2'''
        assert root_elem == root_container_name
    
    @staticmethod
    def priority_is_two_too_constraint(root_elem):
        '''priority=2'''
        assert root_elem == root_container_name
    
    @staticmethod
    def priority_is_negative_constraint(root_elem):
        '''priority=-3'''
        assert root_elem == root_container_name
    
    @staticmethod
    def priority_is_not_int_constraint(root_elem):
        '''priority=cat'''
        assert root_elem == root_container_name
    
    @staticmethod
    def some_constraint(root_elem):
        assert root_elem == root_container_name

class TestBaseConstraintManager():
    def setup_method(self, method):
        self.constraint_manager = BaseConstraintManager(root_container_name, Constraints)
        assert len(self.constraint_manager.constraints) == 7
    
    def test_check_constraints(self):
        self.constraint_manager.check_constraints()

class TestConstraintContainer():
    def setup_method(self, method):
        self.constraint_container = ConstraintContainer()
    
    def test_get_function_priority(self):
        get_priority = self.constraint_container.get_priority
        
        assert get_priority(Constraints.some_constraint) == sys.maxint
        assert get_priority(Constraints.priority_is_one_constraint) == 1
        assert get_priority(Constraints.priority_is_two_constraint) == 2
        assert get_priority(Constraints.priority_is_zero_constraint) == sys.maxint
        assert get_priority(Constraints.priority_is_negative_constraint) == sys.maxint
        assert get_priority(Constraints.priority_is_not_int_constraint) == sys.maxint
    
    def test_append(self):
        self.constraint_container.append(Constraints.some_constraint)
        
        assert len(self.constraint_container) == 1
        assert self.constraint_container[0] == Constraints.some_constraint
    
    def test_append_invalid(self):
        def not_valid():
            pass
        
        self.constraint_container.append(not_valid)
        
        assert len(self.constraint_container.constraints) == 1
        assert self.constraint_container[0] == not_valid
    
    def test_append_with_priority(self):
        self.constraint_container.append(Constraints.priority_is_two_constraint)
        self.constraint_container.append(Constraints.some_constraint)
        self.constraint_container.append(Constraints.priority_is_one_constraint)
        
        assert len(self.constraint_container) == 3
        assert self.constraint_container[0] == Constraints.priority_is_one_constraint
        assert self.constraint_container[1] == Constraints.priority_is_two_constraint
        assert self.constraint_container[2] == Constraints.some_constraint
    
    def test_append_with_same_priority(self):
        self.constraint_container.append(Constraints.priority_is_two_constraint)
        self.constraint_container.append(Constraints.priority_is_two_too_constraint)
        
        assert len(self.constraint_container) == 2
        assert self.constraint_container[0] == Constraints.priority_is_two_constraint
        assert self.constraint_container[1] == Constraints.priority_is_two_too_constraint
    
    def test_append_with_negative_priority(self):
        self.constraint_container.append(Constraints.priority_is_two_constraint)
        self.constraint_container.append(Constraints.priority_is_negative_constraint)
        
        assert len(self.constraint_container) == 2
        assert self.constraint_container[0] == Constraints.priority_is_two_constraint
        assert self.constraint_container[1] == Constraints.priority_is_negative_constraint
    
    def test_container_iter(self):
        test_funcs = (Constraints.priority_is_two_constraint,
                      Constraints.priority_is_not_int_constraint,
                      Constraints.priority_is_one_constraint, )
        expected_funcs = (Constraints.priority_is_one_constraint,
                          Constraints.priority_is_two_constraint,
                          Constraints.priority_is_not_int_constraint)
        self.constraint_container.append(test_funcs[0])
        self.constraint_container.append(test_funcs[1])
        self.constraint_container.append(test_funcs[2])
        
        assert len(self.constraint_container) == 3
        
        for i, func in enumerate(self.constraint_container):
            assert func == expected_funcs[i]
