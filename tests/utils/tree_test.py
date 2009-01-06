# -*- coding: utf-8 -*-
from bui.utils.tree import TreeNode

class TestTreeNode():
    def test_create_tree_node(self):
        tree_node = TreeNode()
    
    def test_append_children_to_tree_node(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        
        tree_node1.children.append(tree_node2)
        
        assert tree_node1.children[0] == tree_node2
        assert tree_node2.parents[0] == tree_node1
    
    def test_append_parents_to_tree_node(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        
        tree_node1.parents.append(tree_node2)
        
        assert tree_node1.parents[0] == tree_node2
        assert tree_node2.children[0] == tree_node1
    
    def test_append_same_node_as_child_and_parent(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        
        tree_node1.children.append(tree_node2)
        tree_node1.parents.append(tree_node2)
        
        assert tree_node1.children[0] == tree_node2
        assert tree_node1.parents[0] == tree_node2
        
        assert tree_node2.children[0] == tree_node1
        assert tree_node2.parents[0] == tree_node1
    
    def test_append_same_node_as_child_multiple_times(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        
        tree_node1.children.append(tree_node2)
        tree_node1.children.append(tree_node2)
        tree_node1.children.append(tree_node2)
        
        assert tree_node1.children[0] == tree_node2
        assert tree_node2.parents[0] == tree_node1
        
        assert len(tree_node1.children) == 1
        assert len(tree_node2.parents) == 1
    
    def test_append_same_node_as_parent_multiple_times(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        
        tree_node1.parents.append(tree_node2)
        tree_node1.parents.append(tree_node2)
        tree_node1.parents.append(tree_node2)
        
        assert tree_node1.parents[0] == tree_node2
        assert tree_node2.children[0] == tree_node1
        
        assert len(tree_node1.parents) == 1
        assert len(tree_node2.children) == 1
    
    def test_remove_child_node(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        
        tree_node1.children.append(tree_node2)
        tree_node1.children.remove(tree_node2)
        
        assert len(tree_node1.children) == 0
        assert len(tree_node2.parents) == 0
    
    def test_remove_parent_node(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        
        tree_node1.parents.append(tree_node2)
        tree_node1.parents.remove(tree_node2)
        
        assert len(tree_node1.parents) == 0
        assert len(tree_node2.children) == 0
    
    def test_remove_same_node_multiple_times(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        
        tree_node1.parents.append(tree_node2)
        tree_node1.parents.remove(tree_node2)
        tree_node1.parents.remove(tree_node2)
        tree_node1.parents.remove(tree_node2)
        
        assert len(tree_node1.parents) == 0
        assert len(tree_node2.children) == 0
    
    def test_find_immediate_child_node(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        tree_node2.name = 'node to be found'
        
        tree_node1.children.append(tree_node2)
        
        assert tree_node1.find_child(name='node to be found') == tree_node2
    
    def test_find_child_node_no_results(self):
        tree_node1 = TreeNode()
        
        assert tree_node1.find_child(name='just some name') == None
    
    def test_find_child_node_from_tree(self):
        tree_node1 = TreeNode()
        tree_node1a = TreeNode()
        tree_node1a1 = TreeNode()
        tree_node1a1.color = 'blue'
        tree_node1a2 = TreeNode()
        tree_node1a2.value = 13
        tree_node1b = TreeNode()
        tree_node1b1 = TreeNode()
        tree_node1b1.find_me = True
        tree_node1b1.color = 'blue'
        
        tree_node1.children.append(tree_node1a)
        tree_node1.children.append(tree_node1b)
        
        tree_node1a.children.append(tree_node1a1)
        tree_node1a.children.append(tree_node1a2)
        
        tree_node1b.children.append(tree_node1b1)
        
        assert tree_node1.find_child(value=13) == tree_node1a2
        assert tree_node1.find_child(find_me=True) == tree_node1b1
        assert tree_node1.find_child(color='blue') == [tree_node1a1, tree_node1b1]
    
    def test_find_immediate_parent_node(self):
        tree_node1 = TreeNode()
        tree_node2 = TreeNode()
        tree_node2.name = 'node to be found'
        
        tree_node1.parents.append(tree_node2)
        
        assert tree_node1.find_parent(name='node to be found') == tree_node2
    
    def test_find_parent_node_no_results(self):
        tree_node1 = TreeNode()
        
        assert tree_node1.find_parent(name='just some name') == None
    
    def test_find_parent_node_from_tree(self):
        tree_node1 = TreeNode()
        tree_node1a = TreeNode()
        tree_node1a1 = TreeNode()
        tree_node1a1.color = 'blue'
        tree_node1a2 = TreeNode()
        tree_node1a2.value = 13
        tree_node1b = TreeNode()
        tree_node1b1 = TreeNode()
        tree_node1b1.find_me = True
        tree_node1b1.color = 'blue'
        
        tree_node1.parents.append(tree_node1a)
        tree_node1.parents.append(tree_node1b)
        
        tree_node1a.parents.append(tree_node1a1)
        tree_node1a.parents.append(tree_node1a2)
        
        tree_node1b.parents.append(tree_node1b1)
        
        assert tree_node1.find_parent(value=13) == tree_node1a2
        assert tree_node1.find_parent(find_me=True) == tree_node1b1
        assert tree_node1.find_parent(color='blue') == [tree_node1a1, tree_node1b1]
