# -*- coding: utf-8 -*-
from bui.container import *
from bui.element import *
from bui.serializer import unserialize

from structure import *

def test_unserialize_valid_structure_with_vertical_child_container():
    root_container = unserialize(StructureWithVerticalContainerChild())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert root_container.visible == True
    assert len(root_container.children) == 1
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.name == 'foobar'
    assert child_container.width == 300
    assert child_container.visible == False

def test_unserialize_valid_structure_with_horizontal_child_container():
    root_container = unserialize(StructureWithHorizontalContainerChild())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 1
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, HorizontalContainer)
    assert child_container.height == 40
    assert child_container.width == 100

def test_unserialize_valid_structure_with_child_container():
    root_container = unserialize(StructureWithMultipleContainers())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 2
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, HorizontalContainer)
    assert child_container.width == 100
    
    child_container = root_container.children[1]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.width == 150

def test_unserialize_valid_structure_with_fill_elements():
    root_container = unserialize(StructureWithFillElements())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 2
    
    child_element = root_container.children[0]
    
    assert isinstance(child_element, Fill)
    assert child_element.width == 100
    
    child_element = root_container.children[1]
    
    assert isinstance(child_element, Fill)
    assert child_element.width == 50

def test_unserialize_valid_structure_with_uistructure():
    root_container = unserialize(StructureWithUIStructure())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 300
    assert len(root_container.children) == 2
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.width == 400
    
    child_element = root_container.children[1]
    
    assert isinstance(child_element, Fill)
    assert child_element.width == 80

def test_unserialize_valid_structure_with_many_vertical_containers():
    root_container = unserialize(StructureWithVerticalContainerChildren())
    
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

def test_unserialize_valid_structure_for_simple_script():
    root_container = unserialize(StructureForSimpleScript())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 400
    assert len(root_container.children) == 3
    
    # add more asserts...
