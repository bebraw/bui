# -*- coding: utf-8 -*-
import sys
from bui.backend.abstract import AbstractNode
import bui.backend.value as value

class TestAbstractNode():
    def test_create_abstract_object(self):
        abstract_object = AbstractNode()
        
        assert abstract_object.children == []
        assert abstract_object.parents == []
        assert abstract_object.parent == None
        
        assert abstract_object.bg_color == None
        assert abstract_object.visible == True
        
        assert abstract_object.x == 0
        assert abstract_object.y == 0
        
        assert abstract_object.width == 0
        assert abstract_object.width_mode == value.AUTO
        assert abstract_object.min_width == 0
        assert abstract_object.max_width == sys.maxint
        
        assert abstract_object.height == 0
        assert abstract_object.width_mode == value.AUTO
        assert abstract_object.min_height == 0
        assert abstract_object.max_height == sys.maxint
    
    def test_visibility(self):
        pass # TODO: validate that if parent is not visible, neither is the child
    
    def test_render(self):
        pass # TODO: (what to test?)
