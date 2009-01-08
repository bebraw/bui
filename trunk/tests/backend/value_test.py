# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractNode
import bui.backend.value as value
from bui.backend.value import ConstrainedValue

possible_values = ('width', 'height', )
class TestConstrainedValue():
    def test_create_constrained_value(self):
        abstract_object = AbstractNode()
        constrained_value = ConstrainedValue('width', abstract_object, value.ABSOLUTE, 5, 2, 20)
    
    def test_auto_mode(self):
        def check(value_name):
            abstract_parent = AbstractNode(width=500, height=500)
            abstract_child = AbstractNode(width=20, width_mode=value.AUTO,
                                            height=20, height_mode=value.AUTO)
            abstract_parent.children.append(abstract_child)
            
            assert getattr(abstract_child, value_name) == 500
            
            abstract_child.max_height = 300
            abstract_child.max_width = 300
            assert getattr(abstract_child, value_name) == 300
            
            abstract_child.min_width = 100
            abstract_child.min_height = 100
            abstract_parent.width = 50
            abstract_parent.height = 50
            assert getattr(abstract_child, value_name) == 100
        
        for possible_value in possible_values:
            yield check, possible_value
    
    def test_absolute_mode(self):
        def check(value_name):
            abstract_parent = AbstractNode(width=500, height=500)
            abstract_child = AbstractNode(width=20, width_mode=value.ABSOLUTE,
                                            height=20, height_mode=value.ABSOLUTE)
            abstract_parent.children.append(abstract_child)
            
            assert getattr(abstract_child, value_name) == 20
        
        for possible_value in possible_values:
            yield check, possible_value
    
    def test_relative_mode(self):
        def check(value_name):
            abstract_parent = AbstractNode(width=500, height=500)
            abstract_child = AbstractNode(width=20, width_mode=value.RELATIVE,
                                            height=20, height_mode=value.RELATIVE)
            abstract_parent.children.append(abstract_child)
            
            assert getattr(abstract_child, value_name) == 100
        
        for possible_value in possible_values:
            yield check, possible_value
