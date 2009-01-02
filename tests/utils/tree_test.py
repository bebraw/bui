# -*- coding: utf-8 -*-
from bui.utils.tree import TreeChild, TreeParent

# TODO: test nasty mixed cases (trees with instances from both classes)

class TestTreeChild():
    def setup_method(self, method):
        self.root_child = TreeChild()
        self.root_child.label = 'root'
        self.child2 = TreeChild(parent=self.root_child)
        self.child2.label = None
        self.child2.name = 'foo_variable'
        self.child3 = TreeChild(parent=self.child2)
        self.child3.label = 'baz child'
        self.child4 = TreeChild(parent=self.child3)
    
    def test_find_parent(self):
        assert self.root_child.find_parent(label='root') is None
        assert self.child4.find_parent(label='root') is self.root_child
        assert self.child4.find_parent(label='baz child') is self.child3
        assert self.child4.find_parent(label=5) is None
        assert self.child3.find_parent(label='baz child') is None
        assert self.child3.find_parent(name='foo_variable') is self.child2
        assert self.child3.find_parent(label='cat', variable=3) is None
        assert self.child4.find_parent() is None
    
    def test_find_root_element(self):
        assert self.child4.find_root_element() is self.root_child
        assert self.root_child.find_root_element() is self.root_child

class TestTreeParent():
    def test_find_child(self):
        parent1 = TreeParent()
        parent1.label = 'first parent'
        parent2 = TreeParent()
        parent2.children = None
        parent2.label = 'second parent'
        parent2.name = 'foo_variable'
        parent3 = TreeParent()
        parent3.children = [parent1, None, parent2, ]
        parent3.label = 'baz parent'
        parent4 = TreeParent()
        parent4.children = [parent3, ]
        parent5 = TreeParent()
        parent5.children = [parent4, ]
        parent6 = TreeParent()
        parent6.children = [parent5, ]
        
        assert parent6.find_child(label='baz parent') is parent3
        assert parent6.find_child(label='first parent') is parent1
        assert parent6.find_child(label='second parent') is parent2
        assert parent6.find_child(name='foo_variable') is parent2
        assert parent6.find_child(label='foobar') is None
        assert parent3.find_child(label='baz parent') is None
        assert parent3.find_child(label=3) is None
        assert parent3.find_child(label=3, name=10) is None
        assert parent3.find_child() is None
    
    def test_append(self):
        parent = TreeParent()
        child = TreeParent()
        
        parent.append(child)
        
        assert len(parent.children) == 1
        assert parent.children[0] == child
    
    def test_remove(self):
        parent = TreeParent()
        child = TreeParent()
        
        parent.append(child)
        parent.remove(child)
        
        assert len(parent.children) == 0
    
    def test_remove_children(self):
        parent = TreeParent()
        child1 = TreeParent()
        child2 = TreeParent()
        
        parent.append(child1)
        parent.append(child2)
        parent.remove_children()
        
        assert len(parent.children) == 0
