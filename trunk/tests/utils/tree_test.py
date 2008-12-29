# -*- coding: utf-8 -*-
from bui.utils.tree import TreeChild, TreeParent

# TODO: test nasty mixed cases (trees with instances from both classes)

class TestTreeChild():
    def setup_method(self, method):
        self.root_child = TreeChild()
        self.root_child.name = 'root'
        self.child2 = TreeChild(parent=self.root_child)
        self.child2.name = None
        self.child2.variable = 'foo_variable'
        self.child3 = TreeChild(parent=self.child2)
        self.child3.name = 'baz_child'
        self.child4 = TreeChild(parent=self.child3)
    
    def test_find_parent(self):
        #assert self.root_child.find_parent(name='root') is None
        assert self.child4.find_parent(name='root') is self.root_child
        assert self.child4.find_parent(name='baz_child') is self.child3
        assert self.child4.find_parent(name=5) is None
        assert self.child3.find_parent(name='baz_child') is None
        assert self.child3.find_parent(variable='foo_variable') is self.child2
        assert self.child3.find_parent(name='cat', variable=3) is None
        assert self.child4.find_parent() is None
    
    def test_find_root_element(self):
        assert self.child4.find_root_element() is self.root_child
        assert self.root_child.find_root_element() is self.root_child

class TestTreeParent():
    def test_find_child(self):
        parent1 = TreeParent()
        parent1.name = 'first_parent'
        parent2 = TreeParent()
        parent2.children = None
        parent2.name = 'second_parent'
        parent2.variable = 'foo_variable'
        parent3 = TreeParent()
        parent3.children = [parent1, None, parent2, ]
        parent3.name = 'baz_parent'
        parent4 = TreeParent()
        parent4.children = [parent3, ]
        parent5 = TreeParent()
        parent5.children = [parent4, ]
        parent6 = TreeParent()
        parent6.children = [parent5, ]
        
        assert parent6.find_child(name='baz_parent') is parent3
        assert parent6.find_child(name='first_parent') is parent1
        assert parent6.find_child(name='second_parent') is parent2
        assert parent6.find_child(variable='foo_variable') is parent2
        assert parent6.find_child(name='foobar') is None
        assert parent3.find_child(name='baz_parent') is None
        assert parent3.find_child(name=3) is None
        assert parent3.find_child(name=3, variable=10) is None
        assert parent3.find_child() is None
