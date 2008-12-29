# -*- coding: utf-8 -*-
from bui.backend.abstract import *
from bui.backend.container import *
from bui.backend.serializer import unserialize

from ..structure import FillElement, MinimalStructure

class TestAbstractObject():
    def test_create_abstract_object(self):
        abstract_object = AbstractObject()
        
        assert abstract_object.name == ''
        
        abstract_object2 = AbstractObject(height=20, name='some name', width=100, foobar=25)
        
        assert abstract_object2.height == 20
        assert abstract_object2.width == 100
        assert hasattr(abstract_object2, 'foobar') == False

class TestAbstractElement():
    def test_create_abstract_element(self):
        abstract_element = AbstractElement()
        
        assert len(abstract_element.children) == 0
        assert abstract_element.event_handler == None
        assert abstract_element.height == 0
        assert abstract_element.width == 0
        assert abstract_element.name == ''
        assert abstract_element.visible == True
        assert abstract_element.variable == None

class TestAbstractContainer():
    def test_create_abstract_container(self):
        abstract_container = AbstractContainer()
        
        assert abstract_container.x_offset == 0
        assert abstract_container.y_offset == 0
        assert abstract_container.event_handler == None
        assert abstract_container.visible == True
        
        abstract_container2 = AbstractContainer(x_offset=100, y_offset=50, visible=False)
        
        assert abstract_container2.x_offset == 100
        assert abstract_container2.y_offset == 50
        assert abstract_container2.visible == False
    
    def test_append(self):
        abstract_container = AbstractContainer()
        
        structure_root = unserialize(MinimalStructure())
        abstract_container.append(structure_root)
        
        assert len(abstract_container.children) == 1
        assert abstract_container.children[0].width == 400
        assert abstract_container.children[0].parent == abstract_container
