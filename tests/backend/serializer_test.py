# -*- coding: utf-8 -*-
from bui.backend.element.fill import Fill
from bui.backend.layout import *
from bui.backend.serializer import unserialize
from bui.backend.window import BaseWindowManager
from ..structure import MinimalStructure, \
                        StructureWithHiddenVerticalLayoutChild, \
                        StructureWithUIStructure, \
                        StructureWithAuto

def test_unserialize_valid_minimal_structure():
    root_container = unserialize(MinimalStructure())
    
    assert isinstance(root_container, VerticalLayout)
    assert root_container.width == 400

def test_unserialize_valid_structure_with_hidden_vertical_child_container():
    root_container = unserialize(StructureWithHiddenVerticalLayoutChild())
    
    assert isinstance(root_container, VerticalLayout)
    assert root_container.width == 200
    assert root_container.visible == True
    assert len(root_container.children) == 1
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalLayout)
    assert child_container.name == 'foobar'
    
    # note that the width of root limits the width of child
    assert child_container.width == 200
    assert child_container.visible == False
    
    child_of_child = child_container.children[0]
    
    assert isinstance(child_of_child, Fill)
    assert child_of_child.width == 200
    assert child_of_child.visible == False

def test_unserialize_valid_structure_with_uistructure():
    root_container = unserialize(StructureWithUIStructure())
    
    assert isinstance(root_container, VerticalLayout)
    assert root_container.width == 300
    assert len(root_container.children) == 2
    
    child_container = root_container.children[0]
    
    # note that the width of root limits the width of child
    assert isinstance(child_container, VerticalLayout)
    assert child_container.width == 300
    
    child_element = root_container.children[1]
    
    assert isinstance(child_element, Fill)
    assert child_element.width == 80

def test_unserialize_structure_with_auto():
    root_container = unserialize(StructureWithAuto())
    
    assert isinstance(root_container, VerticalLayout)
    assert root_container._width == 'auto'
    assert root_container.width == 0
    assert len(root_container.children) == 2
    
    child_fill = root_container.children[0]
    assert isinstance(child_fill, Fill)
    assert child_fill.width == 0
    
    another_child = root_container.children[1]
    assert isinstance(another_child, Fill)
    assert another_child.width == 0
    
    window_manager = BaseWindowManager(width=500)
    root_container.common.window_manager = window_manager
    assert root_container.width == 500
    assert child_fill.width == 500
    assert another_child.width == 50
