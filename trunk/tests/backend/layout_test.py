# -*- coding: utf-8 -*-
from bui.backend.element import Fill
from bui.backend.layout import *
from bui.backend.serializer import unserialize
from bui.backend.window import BaseWindowManager
from ..structure import StructureWithAutoWidth, \
                        StructureWithFreeLayout, \
                        StructureWithHorizontalLayoutNoChildrenWidths, \
                        StructureWithHorizontalLayoutChildrenWidths, \
                        StructureWithHorizontalLayoutPartialChildrenWidths

layout_classes = (FreeLayout, HorizontalLayout, VerticalLayout, )
class TestLayouts():
    def test_create_layout(self):
        def check(layout_name):
            layout = layout_name()
            
            assert layout.children == []
            assert layout.parents == []
            assert layout.parent == None
        
        for layout in layout_classes:
            yield check, layout
    
    def test_append_layout(self):
        def check(layout_name):
            layout1, layout2 = layout_name(), layout_name()
            layout1.append(layout2)
            
            assert layout1.children[0] == layout2
        
        for layout in layout_classes:
            yield check, layout
    
    def test_remove_layout(self):
        def check(layout_name):
            layout1, layout2 = layout_name(), layout_name()
            
            layout1.append(layout2)
            layout1.remove(layout2)
            
            assert len(layout1.children) == 0
            assert len(layout2.parents) == 0
            assert layout2.parent == None
        
        for layout in layout_classes:
            yield check, layout

def test_unserialize_structure_with_free_layout():
    root_layout = unserialize(StructureWithFreeLayout)
    
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
    # assert child_fill_3.width == 800 # XXX
    assert child_fill_3.height == 800

free_configuration = '''
    width: 400
    height: 1000
    structure: root_structure
'''
def test_base_window_manager_with_free_layout():
    window_manager = BaseWindowManager(free_configuration,
                                       structure_document=StructureWithFreeLayout)
    root_layout = window_manager.windows[0].root_layout
    
    assert root_layout.width == 400
    
    child_fill_1 = root_layout.children[0]
    assert child_fill_1.width == 400
    assert child_fill_1.height == 1
    
    child_fill_2 = root_layout.children[1]
    assert child_fill_2.width == 400
    assert child_fill_2.height == 1
    assert child_fill_2.x == 40
    assert child_fill_2.y == 500
    
    child_fill_3 = root_layout.children[2]
    # assert child_fill_3.width == 800 # XXX
    assert child_fill_3.height == 800

free_configuration_with_element_height = '''
    width: 400
    height: 1000
    structure: root_structure
    element_height: 20
'''
def test_base_window_manager_with_free_layout_and_element_height_defined():
    window_manager = BaseWindowManager(free_configuration_with_element_height,
                                       structure_document=StructureWithFreeLayout)
    root_layout = window_manager.windows[0].root_layout
    
    assert root_layout.width == 400
    
    child_fill_1 = root_layout.children[0]
    assert child_fill_1.width == 400
    assert child_fill_1.height == 20
    
    child_fill_2 = root_layout.children[1]
    assert child_fill_2.width == 400
    assert child_fill_2.height == 20
    assert child_fill_2.x == 40
    assert child_fill_2.y == 500
    
    child_fill_3 = root_layout.children[2]
    # assert child_fill_3.width == 800 # XXX
    assert child_fill_3.height == 800

def test_unserialize_structure_with_horizontal_layout_no_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutNoChildrenWidths)
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.width == 100
    assert root_layout.height == 400
    assert root_layout.element_height == 400
    
    root_layout.render()
    
    child_fill_1 = root_layout.children[0]
    assert isinstance(child_fill_1, Fill)
    assert child_fill_1.width == 50
    assert child_fill_1.height == 400
    
    child_fill_2 = root_layout.children[1]
    assert isinstance(child_fill_2, Fill)
    assert child_fill_2.width == 50
    assert child_fill_2.height == 400

configuration_element_height_defined = '''
    width: 500
    height: 1000
    structure: root_structure
    element_height: 20
'''
#unserialize_structure_with_horizontal_layout_no_children_widths_and_element_height_defined
def test_foobar():
    window_manager = BaseWindowManager(configuration_element_height_defined,
                                       structure_document=StructureWithHorizontalLayoutNoChildrenWidths)
    root_layout = window_manager.windows[0].root_layout
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.width == 100
    assert root_layout.height == 400
    assert root_layout.element_height == 500
    
    root_layout.element_height = 70
    
    root_layout.render()
    
    child_fill_1 = root_layout.children[0]
    assert isinstance(child_fill_1, Fill)
    assert child_fill_1.width == 50
    # assert child_fill_1.height == 70 # XXX
    
    child_fill_2 = root_layout.children[1]
    assert isinstance(child_fill_2, Fill)
    assert child_fill_2.width == 50
    # assert child_fill_2.height == 70 # XXX

def test_unserialize_structure_with_horizontal_layout_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutChildrenWidths)
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.width == 200
    
    child_fill_1 = root_layout.children[0]
    assert isinstance(child_fill_1, Fill)
    assert child_fill_1.width == 30
    
    child_fill_2 = root_layout.children[1]
    assert isinstance(child_fill_2, Fill)
    assert child_fill_2.width == 80

def test_unserialize_structure_with_horizontal_layout_partial_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutPartialChildrenWidths)
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.width == 300
    
    root_layout.render()
    
    child_fill_1 = root_layout.children[0]
    assert isinstance(child_fill_1, Fill)
    assert child_fill_1.width == 120
    
    child_fill_2 = root_layout.children[1]
    assert isinstance(child_fill_2, Fill)
    assert child_fill_2.width == 180

# TODO: test predef-free-predef-free case
# TODO: test free-predef-free case

def test_unserialize_structure_with_auto_width():
    root_layout = unserialize(StructureWithAutoWidth)
    
    assert isinstance(root_layout, VerticalLayout)
    assert root_layout.auto_width == True
    assert root_layout.width == 0
    assert root_layout.height == 0
    assert len(root_layout.children) == 2
    
    child_fill = root_layout.children[0]
    assert isinstance(child_fill, Fill)
    assert child_fill.width == 0
    assert child_fill.height == 0
    
    another_child = root_layout.children[1]
    assert isinstance(another_child, Fill)
    assert another_child.width == 0
    assert another_child.height == 0

auto_width_configuration_with_element_height = '''
    width: 500
    height: 1000
    structure: root_structure
    element_height: 20
'''
def test_base_window_manager_with_auto_width_layout_and_element_height_defined():
    window_manager = BaseWindowManager(auto_width_configuration_with_element_height,
                                       structure_document=StructureWithAutoWidth)
    root_layout = window_manager.windows[0].root_layout
    assert root_layout.width == 500
    assert root_layout.height == 40
    
    child_fill = root_layout.children[0]
    assert child_fill.width == 500
    assert child_fill.height == 20
    
    another_child = root_layout.children[1]
    assert another_child.width == 50
    assert another_child.height == 20
