# -*- coding: utf-8 -*-
from bui.backend.abstract import Common
from bui.backend.element.fill import Fill
from bui.backend.layout import *
from bui.backend.serializer import unserialize
from bui.backend.window import BaseWindowManager
from ..structure import MinimalStructure, \
                        StructureWithHiddenVerticalLayoutChild, \
                        StructureWithUIStructure, \
                        StructureWithAuto, \
                        StructureWithFreeLayout, \
                        StructureWithHorizontalLayoutNoChildrenWidths, \
                        StructureWithHorizontalLayoutChildrenWidths, \
                        StructureWithHorizontalLayoutPartialChildrenWidths

# TODO: separate layout specific tests to layout_test.py!

class TestUnserialize():
    def setup_method(self, method):
        common = Common(reset_values=True)
    
    def test_unserialize_valid_minimal_structure(self):
        root_layout = unserialize(MinimalStructure())
        
        assert isinstance(root_layout, VerticalLayout)
        assert root_layout.width == 400
    
    def test_unserialize_valid_structure_with_hidden_vertical_child_container(self):
        root_layout = unserialize(StructureWithHiddenVerticalLayoutChild())
        
        assert isinstance(root_layout, VerticalLayout)
        assert root_layout.width == 200
        assert root_layout.visible == True
        assert len(root_layout.children) == 1
        
        child_container = root_layout.children[0]
        
        assert isinstance(child_container, VerticalLayout)
        assert child_container.name == 'foobar'
        
        # note that the width of root limits the width of child
        assert child_container.width == 200
        assert child_container.visible == False
        
        child_of_child = child_container.children[0]
        
        assert isinstance(child_of_child, Fill)
        assert child_of_child.width == 200
        assert child_of_child.visible == False
    
    def test_unserialize_valid_structure_with_uistructure(self):
        root_layout = unserialize(StructureWithUIStructure())
        
        assert isinstance(root_layout, VerticalLayout)
        assert root_layout.width == 300
        assert len(root_layout.children) == 2
        
        child_container = root_layout.children[0]
        
        # note that the width of root limits the width of child
        assert isinstance(child_container, VerticalLayout)
        assert child_container.width == 300
        
        child_element = root_layout.children[1]
        
        assert isinstance(child_element, Fill)
        assert child_element.width == 80
    
    def test_unserialize_structure_with_free_layout(self):
        root_layout = unserialize(StructureWithFreeLayout())
        
        # note that 20 is the default element height defined at Common
        
        assert isinstance(root_layout, FreeLayout)
        assert root_layout.width == 0
        assert root_layout.height == 20
        
        child_fill_1 = root_layout.children[0]
        assert isinstance(child_fill_1, Fill)
        assert child_fill_1.width == 0
        assert child_fill_1.height == 20
        
        child_fill_2 = root_layout.children[1]
        assert isinstance(child_fill_2, Fill)
        assert child_fill_2.width == 0
        assert child_fill_2.height == 20
        assert child_fill_2.x == 40
        assert child_fill_2.y == 500
        
        child_fill_3 = root_layout.children[2]
        assert isinstance(child_fill_3, Fill)
        print child_fill_3.width
        assert child_fill_3.width == 800
        assert child_fill_3.height == 800
        
        root_layout.common.window_manager = BaseWindowManager(width=400)
        assert root_layout.width == 400
        assert child_fill_1.width == 400
        assert child_fill_2.width == 400
        assert child_fill_2.x == 40
        assert child_fill_2.y == 500
        assert child_fill_3.width == 800
        assert child_fill_3.height == 800
    
    def test_unserialize_structure_with_horizontal_layout_no_children_widths(self):
        root_layout = unserialize(StructureWithHorizontalLayoutNoChildrenWidths())
        
        assert isinstance(root_layout, HorizontalLayout)
        assert root_layout.width == 100
        
        child_fill_1 = root_layout.children[0]
        assert isinstance(child_fill_1, Fill)
        assert child_fill_1.width == 50
        
        child_fill_2 = root_layout.children[1]
        assert isinstance(child_fill_2, Fill)
        assert child_fill_2.width == 50
    
    def test_unserialize_structure_with_horizontal_layout_children_widths(self):
        root_layout = unserialize(StructureWithHorizontalLayoutChildrenWidths())
        
        assert isinstance(root_layout, HorizontalLayout)
        assert root_layout.width == 200
        
        child_fill_1 = root_layout.children[0]
        assert isinstance(child_fill_1, Fill)
        assert child_fill_1.width == 30
        
        child_fill_2 = root_layout.children[1]
        assert isinstance(child_fill_2, Fill)
        assert child_fill_2.width == 80
    
    def test_unserialize_structure_with_horizontal_layout_partial_children_widths(self):
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
    
    def test_unserialize_structure_with_auto(self):
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
        
        root_layout.common.window_manager = BaseWindowManager(width=500)
        assert root_layout.width == 500
        assert child_fill.width == 500
        assert another_child.width == 50
