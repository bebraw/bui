# -*- coding: utf-8 -*-
from bui.backend.layout import BaseLayoutManager
from bui.backend.window import BaseWindowManager

from bui.utils.serializer import unserialize

from tests.structure import HiddenRootContainer, \
                      MultipleVerticalContainers, \
                      StructureWithUIStructure, \
                      StructureWithVerticalContainerChild, \
                      StructureForEventTests \

def test_initialize_layout_with_simple_structure():
    root_container = unserialize(StructureWithUIStructure)
    layout_manager = BaseLayoutManager(BaseWindowManager(), root_container, 20)
    layout_manager.initialize_layout()
    
    manager_root_container = layout_manager.root_container
    
    assert manager_root_container.x == 0
    assert manager_root_container.y == 0
    assert manager_root_container.height == 20
    assert manager_root_container.width == 300
    
def test_initialize_layout_with_structure_having_hidden_container():
    root_container = unserialize(StructureWithVerticalContainerChild)
    layout_manager = BaseLayoutManager(BaseWindowManager(), root_container, 20)
    layout_manager.initialize_layout()
    
    manager_root_container = layout_manager.root_container
    
    assert manager_root_container.x == 0
    assert manager_root_container.y == 0
    assert manager_root_container.height == 0
    assert manager_root_container.width == 200
    
    root_child = manager_root_container.children[0]
    
    assert root_child.x == None
    assert root_child.y == None
    assert root_child.height == 0
    assert root_child.width == 200

def test_initialize_layout_with_structure_having_multiple_children():
    root_container = unserialize(StructureForEventTests)
    layout_manager = BaseLayoutManager(BaseWindowManager(), root_container, 20)
    layout_manager.initialize_layout()
    
    manager_root_container = layout_manager.root_container
    
    assert manager_root_container.x == 0
    assert manager_root_container.y == 0
    assert manager_root_container.height == 80
    assert manager_root_container.width == 200
    
    root_first_child = manager_root_container.children[0]
    
    assert root_first_child.x == 0
    assert root_first_child.y == 0
    assert root_first_child.height == 20
    assert root_first_child.width == 40
    
    root_second_child = manager_root_container.children[1]
    
    assert root_second_child.x == 0
    assert root_second_child.y == 20
    assert root_second_child.height == 20
    assert root_second_child.width == 20
    
    root_third_child = manager_root_container.children[2]
    
    assert root_third_child.x == 0
    assert root_third_child.y == 40
    assert root_third_child.height == 20
    assert root_third_child.width == 200

def test_initialize_layout_with_structure_having_vertical_containers():
    root_container = unserialize(MultipleVerticalContainers)
    layout_manager = BaseLayoutManager(BaseWindowManager(), root_container, 20)
    layout_manager.initialize_layout()
    
    manager_root_container = layout_manager.root_container
    
    assert manager_root_container.x == 0
    assert manager_root_container.y == 0
    assert manager_root_container.height == 140
    assert manager_root_container.width == 200
    
    root_first_child = manager_root_container.children[0]
    
    assert root_first_child.x == 0
    assert root_first_child.y == 0
    assert root_first_child.height == 60
    assert root_first_child.width == 50
    
    root_second_child = manager_root_container.children[1]
    
    assert root_second_child.x == 0
    assert root_second_child.y == 60
    assert root_second_child.height == 80
    assert root_second_child.width == 200

def test_initialize_layout_with_hidden_structures():
    root_container = unserialize(HiddenRootContainer)
    layout_manager = BaseLayoutManager(BaseWindowManager(), root_container, 20)
    layout_manager.initialize_layout()
    
    manager_root_container = layout_manager.root_container
    
    assert manager_root_container.x == None
    assert manager_root_container.y == None
    assert manager_root_container.height == 0
    assert manager_root_container.width == 300
    
    root_child = manager_root_container.children[0]
    
    assert root_child.x == None
    assert root_child.y == None
    assert root_child.height == 0
    assert root_child.width == 300
    
    root_child_child = root_child.children[0]
    
    assert root_child_child.x == None
    assert root_child_child.y == None
    assert root_child_child.height == 0
    assert root_child_child.width == 300
    
    for child in root_child_child.children:
        assert child.x == None
        assert child.y == None
        assert child.height == 0
        assert child.width == 100
