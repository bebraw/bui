# -*- coding: utf-8 -*-
from bui.backend.element import Fill
from bui.backend.layout import *
from bui.backend.serializer import unserialize
from ..structure import MinimalStructure, \
                        StructureWithHiddenVerticalLayoutChild, \
                        StructureWithUIStructure

def test_unserialize_valid_minimal_structure():
    root_layout = unserialize(MinimalStructure())
    
    assert isinstance(root_layout, VerticalLayout)
    assert root_layout.render_node.width == 400

def test_unserialize_valid_structure_with_hidden_vertical_child_container():
    root_layout = unserialize(StructureWithHiddenVerticalLayoutChild())
    
    assert isinstance(root_layout, VerticalLayout)
    assert root_layout.render_node.width == 200
    assert root_layout.render_node.visible == True
    assert len(root_layout.render_node.children) == 1
    
    child_container = root_layout.render_node.children[0]
    
    assert isinstance(child_container, VerticalLayoutNode)
    #assert child_container.name == 'foobar' # XXX: should node know its container?
    
    # note that the width of root limits the width of child
    assert child_container.width == 200
    assert child_container.visible == False
    
    child_of_child = child_container.children[0]
    
    assert isinstance(child_of_child, RenderNode)
    assert child_of_child.width == 200
    assert child_of_child.visible == False

def test_unserialize_valid_structure_with_uistructure():
    root_layout = unserialize(StructureWithUIStructure())
    
    assert isinstance(root_layout, VerticalLayout)
    assert root_layout.render_node.width == 300
    assert len(root_layout.render_node.children) == 2
    
    child_container = root_layout.render_node.children[0]
    
    # note that the width of root limits the width of child
    assert isinstance(child_container, VerticalLayoutNode)
    assert child_container.width == 300
    
    child_element = root_layout.render_node.children[1]
    
    assert isinstance(child_element, RenderNode)
    assert child_element.width == 80
