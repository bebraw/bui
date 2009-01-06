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

# TODO: generalize and combine tests!!! (esp. free/horizontal/vertical layout) (table based testing???)

class TestLayoutNode():
    def test_create_layout_node(self):
        layout_node = LayoutNode()
        
        assert layout_node.element_width == None
        assert layout_node.element_height == None
        assert layout_node.children == []
        assert layout_node.parents == []
        assert layout_node.parent == None
    
    def test_append_layout_node(self):
        layout_node1, layout_node2 = LayoutNode(), LayoutNode()
        
        layout_node1.append(layout_node2)
        
        assert layout_node1.children[0] == layout_node2
        assert layout_node2.parents[0] == layout_node1
        assert layout_node2.parent == layout_node1
    
    def test_remove_render_node(self):
        layout_node1, layout_node2 = LayoutNode(), LayoutNode()
        
        layout_node1.append(layout_node2)
        layout_node1.remove(layout_node2)
        
        assert len(layout_node1.children) == 0
        assert len(layout_node2.parents) == 0
        assert layout_node2.parent == None

class TestFreeLayout():
    def test_create_free_layout(self):
        free_layout = FreeLayout()
        
        assert isinstance(free_layout.render_node, FreeLayoutNode)
    
    def test_append_free_layout(self):
        free_layout1, free_layout2 = FreeLayout(), FreeLayout()
        
        free_layout1.append(free_layout2)
        
        assert free_layout1.render_node.children[0] == free_layout2.render_node
    
    def test_remove_free_layout(self):
        free_layout1, free_layout2 = FreeLayout(), FreeLayout()
        
        free_layout1.append(free_layout2)
        free_layout1.remove(free_layout2)
        
        assert len(free_layout1.render_node.children) == 0
        assert len(free_layout2.render_node.parents) == 0
        assert free_layout2.render_node.parent == None

class TestHorizontalLayout():
    def test_create_horizontal_layout(self):
        horizontal_layout = HorizontalLayout()
        
        assert isinstance(horizontal_layout.render_node, HorizontalLayoutNode)
    
    def test_append_horizontal_layout(self):
        horizontal_layout1, horizontal_layout2 = HorizontalLayout(), HorizontalLayout()
        
        horizontal_layout1.append(horizontal_layout2)
        
        assert horizontal_layout1.render_node.children[0] == horizontal_layout2.render_node
    
    def test_remove_horizontal_layout(self):
        horizontal_layout1, horizontal_layout2 = HorizontalLayout(), HorizontalLayout()
        
        horizontal_layout1.append(horizontal_layout2)
        horizontal_layout1.remove(horizontal_layout2)
        
        assert len(horizontal_layout1.render_node.children) == 0
        assert len(horizontal_layout2.render_node.parents) == 0
        assert horizontal_layout2.render_node.parent == None

class TestVerticalLayout():
    def test_create_vertical_layout(self):
        vertical_layout = VerticalLayout()
        
        assert isinstance(vertical_layout.render_node, VerticalLayoutNode)
    
    def test_append_vertical_layout(self):
        vertical_layout1, vertical_layout2 = VerticalLayout(), VerticalLayout()
        
        vertical_layout1.append(vertical_layout2)
        
        assert vertical_layout1.render_node.children[0] == vertical_layout2.render_node
    
    def test_remove_vertical_layout(self):
        vertical_layout1, vertical_layout2 = VerticalLayout(), VerticalLayout()
        
        vertical_layout1.append(vertical_layout2)
        vertical_layout1.remove(vertical_layout2)
        
        assert len(vertical_layout1.render_node.children) == 0
        assert len(vertical_layout2.render_node.parents) == 0
        assert vertical_layout2.render_node.parent == None

def test_unserialize_structure_with_free_layout():
    root_layout = unserialize(StructureWithFreeLayout)
    
    assert isinstance(root_layout, FreeLayout)
    assert root_layout.render_node.width == 0
    assert root_layout.render_node.height == 0
    
    child_fill_1 = root_layout.render_node.children[0]
    assert isinstance(child_fill_1, RenderNode)
    assert child_fill_1.width == 0
    assert child_fill_1.height == 0
    
    child_fill_2 = root_layout.render_node.children[1]
    assert isinstance(child_fill_2, RenderNode)
    assert child_fill_2.width == 0
    assert child_fill_2.height == 0
    assert child_fill_2.x == 40
    assert child_fill_2.y == 500
    
    child_fill_3 = root_layout.render_node.children[2]
    assert isinstance(child_fill_3, RenderNode)
    # assert child_fill_3.width == 800 # XXX
    assert child_fill_3.height == 800

free_configuration = '''
    width: 400
    height: 1000
    structure: root_structure
'''
def test_base_window_manager_with_free_layout():
    window_manager = BaseWindowManager(free_configuration, structure_document=StructureWithFreeLayout)
    root_layout = window_manager.windows[0].root_layout
    
    assert root_layout.render_node.width == 400
    
    child_fill_1 = root_layout.render_node.children[0]
    assert child_fill_1.width == 400
    assert child_fill_1.height == 1
    
    child_fill_2 = root_layout.render_node.children[1]
    assert child_fill_2.width == 400
    assert child_fill_2.height == 1
    assert child_fill_2.x == 40
    assert child_fill_2.y == 500
    
    child_fill_3 = root_layout.render_node.children[2]
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
    
    assert root_layout.render_node.width == 400
    
    child_fill_1 = root_layout.render_node.children[0]
    assert child_fill_1.width == 400
    assert child_fill_1.height == 20
    
    child_fill_2 = root_layout.render_node.children[1]
    assert child_fill_2.width == 400
    assert child_fill_2.height == 20
    assert child_fill_2.x == 40
    assert child_fill_2.y == 500
    
    child_fill_3 = root_layout.render_node.children[2]
    # assert child_fill_3.width == 800 # XXX
    assert child_fill_3.height == 800

def test_unserialize_structure_with_horizontal_layout_no_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutNoChildrenWidths)
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.render_node.width == 100
    assert root_layout.render_node.height == 400
    assert root_layout.render_node.element_height == 400
    
    root_layout.render()
    
    child_fill_1 = root_layout.render_node.children[0]
    assert isinstance(child_fill_1, RenderNode)
    assert child_fill_1.width == 50
    assert child_fill_1.height == 400
    
    child_fill_2 = root_layout.render_node.children[1]
    assert isinstance(child_fill_2, RenderNode)
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
    assert root_layout.render_node.width == 100
    assert root_layout.render_node.height == 400
    assert root_layout.render_node.element_height == 500
    
    root_layout.element_height = 70
    
    root_layout.render()
    
    child_fill_1 = root_layout.render_node.children[0]
    assert isinstance(child_fill_1, RenderNode)
    assert child_fill_1.width == 50
    # assert child_fill_1.height == 70 # XXX
    
    child_fill_2 = root_layout.render_node.children[1]
    assert isinstance(child_fill_2, RenderNode)
    assert child_fill_2.width == 50
    # assert child_fill_2.height == 70 # XXX

def test_unserialize_structure_with_horizontal_layout_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutChildrenWidths)
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.render_node.width == 200
    
    child_fill_1 = root_layout.render_node.children[0]
    assert isinstance(child_fill_1, RenderNode)
    assert child_fill_1.width == 30
    
    child_fill_2 = root_layout.render_node.children[1]
    assert isinstance(child_fill_2, RenderNode)
    assert child_fill_2.width == 80

def test_unserialize_structure_with_horizontal_layout_partial_children_widths():
    root_layout = unserialize(StructureWithHorizontalLayoutPartialChildrenWidths)
    
    assert isinstance(root_layout, HorizontalLayout)
    assert root_layout.render_node.width == 300
    
    root_layout.render()
    
    child_fill_1 = root_layout.render_node.children[0]
    assert isinstance(child_fill_1, RenderNode)
    assert child_fill_1.width == 120
    
    child_fill_2 = root_layout.render_node.children[1]
    assert isinstance(child_fill_2, RenderNode)
    assert child_fill_2.width == 180

# TODO: test predef-free-predef-free case
# TODO: test free-predef-free case

def test_unserialize_structure_with_auto_width():
    root_layout = unserialize(StructureWithAutoWidth)
    
    assert isinstance(root_layout, VerticalLayout)
    assert root_layout.render_node.auto_width == True
    assert root_layout.render_node.width == 0
    assert root_layout.render_node.height == 0
    assert len(root_layout.render_node.children) == 2
    
    child_fill = root_layout.render_node.children[0]
    assert isinstance(child_fill, RenderNode)
    assert child_fill.width == 0
    assert child_fill.height == 0
    
    another_child = root_layout.render_node.children[1]
    assert isinstance(another_child, RenderNode)
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
    assert root_layout.render_node.width == 500
    assert root_layout.render_node.height == 40
    
    child_fill = root_layout.render_node.children[0]
    assert child_fill.width == 500
    assert child_fill.height == 20
    
    another_child = root_layout.render_node.children[1]
    assert another_child.width == 50
    assert another_child.height == 20
