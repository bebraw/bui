# -*- coding: utf-8 -*-
from bui.container import HorizontalContainer, VerticalContainer
from bui.parser import read_yaml
from bui.treehelper import TreeHelper

from structure import structure_vertical_container_children, structure_with_multiple_containers

class TestTreeHelper():
    def setup_method(self, method):
        dict = read_yaml(structure_vertical_container_children)
        self.tree_helper = TreeHelper(globals(), dict)
    
    def test_add_child_structure(self):
        child_root = self.tree_helper.add_child_structure(structure_with_multiple_containers, 'foobar')
        
        assert isinstance(child_root, VerticalContainer)
        assert child_root.parent == self.tree_helper
    
    def test_find_index_of_last_child(self):
        index = self.tree_helper._find_index_of_last_child(name='foobar')
        
        #assert len(self.tree_helper.children) == 4 # this needs to be tested some other way. perhaps move treehelper to container??? elements need some of the funcs too (find_element, find_parent!)
        #assert index == 3
    
    def test_find_parent(self):
        pass
    
    def test_find_root_element(self):
        pass
    
    def test_find_child(self):
        pass
