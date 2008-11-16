# -*- coding: utf-8 -*-
from bui.abstract import *

class TestAbstractObject():
    def test_create_abstract_object(self):
        abstract_object = AbstractObject()
        
        assert abstract_object.name == ''
        
        args = {'height': 20, 'name': 'some name', 'width': 100, 'foobar': 25}
        abstract_object2 = AbstractObject(args)
        
        assert abstract_object2.height == 20
        assert abstract_object2.width == 100
        assert hasattr(abstract_object2, 'foobar') == False

class TestAbstractElement():
    def test_create_abstract_element(self):
        abstract_element = AbstractElement()
        
        assert len(abstract_element.children) == 0
        assert abstract_element.event_handler == None
        assert abstract_element.height == None
        assert abstract_element.width == None
        assert abstract_element.name == ''
        assert abstract_element.visible == True
        assert abstract_element.variable == None
