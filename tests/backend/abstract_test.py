# -*- coding: utf-8 -*-
import sys
from bui.backend.abstract import AbstractObject

class TestAbstractObject():
    def test_create_abstract_object(self):
        abstract_object = AbstractObject()
        
        assert abstract_object.children == []
        assert abstract_object.parents == []
        assert abstract_object.parent == None
        
        assert abstract_object.bg_color == None
        assert abstract_object.visible == True
        
        assert abstract_object.x == 0
        assert abstract_object.y == 0
        
        # TODO: refactor
        assert abstract_object.auto_width ==  False
        assert abstract_object.width == 0
        assert abstract_object.min_width == 0
        assert abstract_object.max_width == sys.maxint
        
        # TODO: refactor
        assert abstract_object.auto_height == False
        assert abstract_object.height == 0
        assert abstract_object.min_height == 0
        assert abstract_object.max_height == sys.maxint
    
    # width
    # height
    # visibility
    # render
