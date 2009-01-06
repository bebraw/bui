# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self):
        self.children = NodeContainer(self, complementary_items_name='parents')
        self.parents = NodeContainer(self, complementary_items_name='children')
    
    def find_child(self, **kvargs):
        return self._generic_find(item_to_find='children', **kvargs)
    
    def find_parent(self, **kvargs):
        return self._generic_find(item_to_find='parents', **kvargs)
    
    def find_root_node(self):
        return self._generic_find(item_to_find='parents', parents=[])
    
    def _generic_find(self, item_to_find, **kvargs):
        found_nodes = self._generic_recursion(item_to_find, kvargs, [], [])
        return self._check_found_nodes(found_nodes)
    
    def _generic_recursion(self, items_name, search_clauses, found_nodes, visited_nodes):
        visited_nodes.append(self)
        items = getattr(self, items_name)
        
        for item in items:
            try:
                all_match = True
                for wanted_attribute, wanted_value in search_clauses.items():
                    attribute = getattr(item, wanted_attribute)
                    
                    if attribute != wanted_value:
                        all_match = False
                        break
                
                if all_match:
                    found_nodes.append(item)
            except AttributeError:
                pass
            
            if item not in visited_nodes:
                item._generic_recursion(items_name, search_clauses, found_nodes, visited_nodes)
        
        return found_nodes
    
    def _check_found_nodes(self, found_nodes):
        if len(found_nodes) == 1:
            return found_nodes[0]
        
        if len(found_nodes) == 0:
            return None
        
        return found_nodes

class NodeContainer(list):
    def __init__(self, owner, complementary_items_name):
        super(NodeContainer, self).__init__()
        self.owner = owner
        self.complementary_items_name = complementary_items_name
    
    def append(self, *items):
        for item in items:
            if item not in self:
                super(NodeContainer, self).append(item)
                complementary_items = getattr(item, self.complementary_items_name)
                complementary_items.append(self.owner)
    
    def remove(self, *items):
        for item in items:
            if item in self:
                super(NodeContainer, self).remove(item)
                complementary_items = getattr(item, self.complementary_items_name)
                complementary_items.remove(self.owner)
