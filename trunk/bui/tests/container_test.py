# -*- coding: utf-8 -*-
from bui.container import *
from bui.element import EmptyElement

from structure import minimal_structure, empty_element

class TestAbstractContainer():
    def test_create_abstract_container(self):
        abstract_container = AbstractContainer()
        
        assert abstract_container.x_offset == 0
        assert abstract_container.y_offset == 0
        assert abstract_container.event_handler == None
        assert abstract_container.visible == True
        
        args = {'x_offset': 100, 'y_offset': 50, 'visible': False}
        abstract_container2 = AbstractContainer(args)
        
        assert abstract_container2.x_offset == 100
        assert abstract_container2.y_offset == 50
        assert abstract_container2.visible == False
    
    def test_add_child_structure(self):
        abstract_container = AbstractContainer()
        
        abstract_container.add_child_structure(minimal_structure, globals())
        
        assert len(abstract_container.children) == 1
        assert abstract_container.children[0].width == 400
        assert abstract_container.children[0].parent == abstract_container
    
    def test_has_only_container_children(self):
        abstract_container = AbstractContainer()
        assert abstract_container.has_only_container_children() == False
        
        abstract_container.add_child_structure(minimal_structure, globals())
        assert abstract_container.has_only_container_children() == True
        
        abstract_container2 = AbstractContainer()
        abstract_container2.add_child_structure(empty_element, globals())
        assert abstract_container2.has_only_container_children() == False
    
    def test_initialize_element_heights(self):
        pass
    
    def test_calculate_children_widths(self):
        pass
    
    def test_initialize_element_widths(self):
        pass

class TestEmptyContainer():
    def test_render(self):
        container = EmptyContainer()
        #container.render(None) # need to pass real coord here
        # assert that coord has not changed

class TestHorizontalContainer():
    def test_render(self):
        container = HorizontalContainer()
        #container.render(None) # need to pass real coord here
        # assert the change of coord

class TestVerticalContainer():
    def test_render(self):
        container = VerticalContainer()
        #container.render(None) # need to pass real coord here
        # assert the change of coord
