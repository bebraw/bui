# -*- coding: utf-8 -*-
from bui.container import HorizontalContainer, VerticalContainer
from bui.parser import read_yaml
from bui.tree import TreeChild, TreeParent

from structure import structure_vertical_container_children, structure_with_multiple_containers

class TestTreeChild():
    def setup_method(self, method):
        dict = read_yaml(structure_vertical_container_children)
        #self.tree_child = TreeChild(globals(), dict)
    
    def test_find_parent(self):
        pass
    
    def test_find_root_element(self):
        pass

class TestTreeParent():
    def setup_method(self, method):
        dict = read_yaml(structure_vertical_container_children)
        self.tree_parent = TreeParent(globals(), dict)
    
    def test_add_child_structure(self):
        child_root = self.tree_parent.add_child_structure(structure_with_multiple_containers, 'foobar')
        
        assert isinstance(child_root, VerticalContainer)
        assert child_root.parent == self.tree_parent
    
    def test_find_index_of_last_child(self):
        index = self.tree_parent._find_index_of_last_child(name='foobar')
        
        #assert len(self.tree_helper.children) == 4 # this needs to be tested some other way. perhaps move treehelper to container??? elements need some of the funcs too (find_element, find_parent!)
        #assert index == 3
    
    def test_find_child(self):
        pass
