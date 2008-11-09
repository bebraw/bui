# -*- coding: utf-8 -*-
from bui.container import VerticalContainer
from bui.element import EmptyElement
from bui.serializer import serialize

from structure import *

def test_serialize():
    root_container = serialize(structure_with_uistructure, globals())
    assert isinstance(root_container, VerticalContainer)

def test_serialize_valid_minimal_structure():
    root_container = serialize(minimal_structure, globals())
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 400

def test_serialize_valid_structure_with_child_container():
    root_container = serialize(structure_vertical_container_child, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert root_container.visible == True
    assert len(root_container.children) == 1
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.name == 'foobar'
    assert child_container.width == 300
    assert child_container.visible == False

def test_serialize_valid_structure_with_child_container():
    root_container = serialize(structure_horizontal_container_child, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 1
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, HorizontalContainer)
    assert child_container.height == 40
    assert child_container.width == 100

def test_serialize_valid_structure_with_child_container():
    root_container = serialize(structure_with_multiple_containers, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 2
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, HorizontalContainer)
    assert child_container.width == 100
    
    child_container = root_container.children[1]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.width == 150

def test_serialize_valid_structure_with_child_container():
    root_container = serialize(structure_with_empty_elements, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 2
    
    child_element = root_container.children[0]
    
    assert isinstance(child_element, EmptyElement)
    assert child_element.width == 100
    
    child_element = root_container.children[1]
    
    assert isinstance(child_element, EmptyElement)
    assert child_element.width == 50

def test_serialize_valid_structure_with_uistructure():
    root_container = serialize(structure_with_uistructure, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 300
    assert len(root_container.children) == 2
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.width == 400
    
    child_element = root_container.children[1]
    
    assert isinstance(child_element, EmptyElement)
    assert child_element.width == 80

def test_serialize_valid_structure_with_many_vertical_containers():
    root_container = serialize(structure_vertical_container_children, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 4
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.name == 'foobar'
    assert child_container.visible == False
    assert child_container.width == 50
    
    child_container = root_container.children[1]
    
    assert child_container.name == 'foobar'
    
    child_container = root_container.children[2]
    
    assert child_container.name == 'foobar'
    
    child_container = root_container.children[3]
    
    assert child_container.name == 'barbar'
