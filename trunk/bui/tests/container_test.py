# -*- coding: utf-8 -*-
from bui.container import *

class TestAbstractContainer():
    def setup_method(self, method):
        pass
    
    def test_add_child_structure(self):
        pass
    
    def test_has_only_container_children(self):
        pass
    
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
