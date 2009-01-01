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
                        StructureWithFreeLayout

class TestUnserialize():
    def setup_method(self, method):
        common = Common(reset_values=True)
    
    def test_unserialize_valid_minimal_structure(self):
        root_container = unserialize(MinimalStructure())
        
        assert isinstance(root_container, VerticalLayout)
        assert root_container.width == 400
    
    def test_unserialize_valid_structure_with_hidden_vertical_child_container(self):
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
    
    def test_unserialize_valid_structure_with_uistructure(self):
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
    
    def test_unserialize_structure_with_auto(self):
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
        
        root_container.common.window_manager = BaseWindowManager(width=500)
        assert root_container.width == 500
        assert child_fill.width == 500
        assert another_child.width == 50
    
    def test_unserialize_structure_with_free_layout(self):
        root_container = unserialize(StructureWithFreeLayout())
        
        # note that 20 is the default element height defined at Common
        
        assert isinstance(root_container, FreeLayout)
        assert root_container.width == 0
        assert root_container.height == 20
        
        child_fill_1 = root_container.children[0]
        assert isinstance(child_fill_1, Fill)
        assert child_fill_1.width == 0
        assert child_fill_1.height == 20
        
        child_fill_2 = root_container.children[1]
        assert isinstance(child_fill_2, Fill)
        assert child_fill_2.width == 0
        assert child_fill_2.height == 20
        assert child_fill_2.x == 40
        assert child_fill_2.y == 500
        
        child_fill_3 = root_container.children[2]
        assert isinstance(child_fill_3, Fill)
        print child_fill_3.width
        assert child_fill_3.width == 800
        assert child_fill_3.height == 800
        
        root_container.common.window_manager = BaseWindowManager(width=400)
        assert root_container.width == 400
        assert child_fill_1.width == 400
        assert child_fill_2.width == 400
        assert child_fill_2.x == 40
        assert child_fill_2.y == 500
        assert child_fill_3.width == 800
        assert child_fill_3.height == 800
