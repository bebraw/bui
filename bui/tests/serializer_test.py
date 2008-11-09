# -*- coding: utf-8 -*-
from bui.container import *
from bui.element import EmptyElement
from bui.serializer import unserialize

from bui.blender.element import *

from structure import *

def test_unserialize():
    root_container = unserialize(structure_with_uistructure, globals())
    assert isinstance(root_container, VerticalContainer)

def test_unserialize_valid_minimal_structure():
    root_container = unserialize(minimal_structure, globals())
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 400

def test_unserialize_valid_structure_with_child_container():
    root_container = unserialize(structure_vertical_container_child, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert root_container.visible == True
    assert len(root_container.children) == 1
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.name == 'foobar'
    assert child_container.width == 300
    assert child_container.visible == False

def test_unserialize_valid_structure_with_child_container():
    root_container = unserialize(structure_horizontal_container_child, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 1
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, HorizontalContainer)
    assert child_container.height == 40
    assert child_container.width == 100

def test_unserialize_valid_structure_with_child_container():
    root_container = unserialize(structure_with_multiple_containers, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 2
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, HorizontalContainer)
    assert child_container.width == 100
    
    child_container = root_container.children[1]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.width == 150

def test_unserialize_valid_structure_with_child_container():
    root_container = unserialize(structure_with_empty_elements, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 2
    
    child_element = root_container.children[0]
    
    assert isinstance(child_element, EmptyElement)
    assert child_element.width == 100
    
    child_element = root_container.children[1]
    
    assert isinstance(child_element, EmptyElement)
    assert child_element.width == 50

def test_unserialize_valid_structure_with_uistructure():
    root_container = unserialize(structure_with_uistructure, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 300
    assert len(root_container.children) == 2
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.width == 400
    
    child_element = root_container.children[1]
    
    assert isinstance(child_element, EmptyElement)
    assert child_element.width == 80

def test_unserialize_valid_structure_with_many_vertical_containers():
    root_container = unserialize(structure_vertical_container_children, globals())
    
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

'''
VerticalContainer:
    name: root_vertical
    width: 400
    children:
        - HorizontalContainer:
            name: test_hori
            children:
                - Label:
                    name: Test script
                - PushButton:
                    name: X
                    tooltip: Quit script
                    event_handler: quit_script
                    width: 20
        - EmptyContainer:
            name: empty_cont
            height: 10
        - HorizontalContainer:
            name: last_hori
            children:
                - PushButton:
                    name: Do something
                    tooltip: Add some tool here
                    width: 100
'''
def test_unserialize_valid_structure_for_simple_script():
    root_container = unserialize(structure_for_simple_script, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 400
    assert len(root_container.children) == 3
    
    # add more asserts...
