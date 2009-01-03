# -*- coding: utf-8 -*-
from bui.backend.element.fill import Fill
from bui.backend.layout import *
from bui.backend.serializer import unserialize
from bui.backend.window import BaseWindowManager
from ..structure import StructureWithAuto, \
                        StructureWithFreeLayout, \
                        StructureWithHorizontalLayoutNoChildrenWidths, \
                        StructureWithHorizontalLayoutChildrenWidths, \
                        StructureWithHorizontalLayoutPartialChildrenWidths

def test_unserialize_structure_with_free_layout():
    root_layout = unserialize(StructureWithFreeLayout())
    
    assert isinstance(root_layout, FreeLayout)
    assert root_layout.width == 0
    assert root_layout.height == 0
    
    child_fill_1 = root_layout.children[0]
    assert isinstance(child_fill_1, Fill)
    assert child_fill_1.width == 0
    assert child_fill_1.height == 0
    
    child_fill_2 = root_layout.children[1]
    assert isinstance(child_fill_2, Fill)
    assert child_fill_2.width == 0
    assert child_fill_2.height == 0
    assert child_fill_2.x == 40
    assert child_fill_2.y == 500
    
    child_fill_3 = root_layout.children[2]
    assert isinstance(child_fill_3, Fill)
    print child_fill_3.width
    assert child_fill_3.width == 800
    assert child_fill_3.height == 800
    
    # XXX: case in which structure is attached to a BaseWindow
    #root_layout.common.window_manager = BaseWindowManager(width=400)
    #assert root_layout.width == 400
    #assert child_fill_1.width == 400
    #assert child_fill_2.width == 400
    #assert child_fill_2.x == 40
    #assert child_fill_2.y == 500
    #assert child_fill_3.width == 800
    #assert child_fill_3.height == 800

# TODO: test case in which element_height has been defined in config!

def test_unserialize_structure_with_horizontal_layout_no_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutNoChildrenWidths())
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.width == 100
    
    child_fill_1 = root_layout.children[0]
    assert isinstance(child_fill_1, Fill)
    assert child_fill_1.width == 50
    
    child_fill_2 = root_layout.children[1]
    assert isinstance(child_fill_2, Fill)
    assert child_fill_2.width == 50

def test_unserialize_structure_with_horizontal_layout_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutChildrenWidths())
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.width == 200
    
    child_fill_1 = root_layout.children[0]
    assert isinstance(child_fill_1, Fill)
    assert child_fill_1.width == 30
    
    child_fill_2 = root_layout.children[1]
    assert isinstance(child_fill_2, Fill)
    assert child_fill_2.width == 80

def test_unserialize_structure_with_horizontal_layout_partial_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutPartialChildrenWidths())
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.width == 300
    
    child_fill_1 = root_layout.children[0]
    assert isinstance(child_fill_1, Fill)
    assert child_fill_1.width == 120
    
    child_fill_2 = root_layout.children[1]
    assert isinstance(child_fill_2, Fill)
    print child_fill_2.width
    assert child_fill_2.width == 180

# TODO: test predef-free-predef-free case
# TODO: test free-predef-free case

def test_unserialize_structure_with_auto():
    root_layout = unserialize(StructureWithAuto())
    
    assert isinstance(root_layout, VerticalLayout)
    assert root_layout._width == 'auto'
    assert root_layout.width == 0
    assert len(root_layout.children) == 2
    
    child_fill = root_layout.children[0]
    assert isinstance(child_fill, Fill)
    assert child_fill.width == 0
    
    another_child = root_layout.children[1]
    assert isinstance(another_child, Fill)
    assert another_child.width == 0
    
    # XXX: case in which structure is attached to a BaseWindow
    #root_layout.common.window_manager = BaseWindowManager(width=500)
    #assert root_layout.width == 500
    #assert child_fill.width == 500
    #assert another_child.width == 50
