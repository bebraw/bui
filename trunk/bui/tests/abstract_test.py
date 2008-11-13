# -*- coding: utf-8 -*-
from bui.abstract import *

class TestAbstractObject():
    def test_create_abstract_object(self):
        abstract_object = AbstractObject()
        
        assert abstract_object.name == ''
        assert abstract_object.visible == True
        
        def foo():
            print 'foo'
        
        args = {'event_handler': foo, 'height': 20, 'name': 'some name',
                'visible': False, 'width': 100, 'foobar': 25}
        abstract_object2 = AbstractObject(args)
        
        assert abstract_object2.event_handler == foo
        assert abstract_object2.height == 20
        assert abstract_object2.name == 'some name'
        assert abstract_object2.visible == False
        assert abstract_object2.width == 100
        assert hasattr(abstract_object2, 'foobar') == False

class TestAbstractElement():
    def test_create_abstract_element(self):
        abstract_element = AbstractElement()
        
        assert len(abstract_element.children) == 0
