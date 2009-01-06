# -*- coding: utf-8 -*-

# TODO: rename this module as node! (TreeNode -> Node!)

# TODO: make this generic so multiple attributes can be checked at once!
def parse_kvargs(**kvargs):
    if len(kvargs) == 1:
        arg_key = kvargs.keys()[0]
        arg_value = kvargs.values()[0]
        
        return arg_key, arg_value
    raise ValueError

# TODO: add find_root, remove_children, remove_parents?
class TreeNode(object):
    def __init__(self):
        self.children = TreeNodeContainer(self, complementary_items_name='parents')
        self.parents = TreeNodeContainer(self, complementary_items_name='children')
    
    def find_child(self, **kvargs):
        return self._generic_find(item_to_find='children', **kvargs)
    
    def find_parent(self, **kvargs):
        return self._generic_find(item_to_find='parents', **kvargs)
    
    def _generic_find(self, item_to_find, **kvargs):
        try:
            arg_key, arg_value = parse_kvargs(**kvargs)
            found_nodes = self._generic_recursion(item_to_find, arg_key, arg_value, [])
            
            return self.check_found_nodes(found_nodes)
        except ValueError:
            pass
    
    def _generic_recursion(self, items_name, wanted_attribute, wanted_value, found_nodes):
        items = getattr(self, items_name)
        
        for item in items:
            try:
                attribute = getattr(item, wanted_attribute)
                
                if attribute == wanted_value:
                    found_nodes.append(item)
            except AttributeError:
                pass
            
            item._generic_recursion(items_name, wanted_attribute, wanted_value, found_nodes)
        
        return found_nodes
    
    def check_found_nodes(self, found_nodes):
        if len(found_nodes) == 1:
            return found_nodes[0]
        
        if len(found_nodes) == 0:
            return None
        
        return found_nodes

class TreeNodeContainer(list):
    def __init__(self, owner, complementary_items_name):
        super(TreeNodeContainer, self).__init__()
        self.owner = owner
        self.complementary_items_name = complementary_items_name
    
    def append(self, item):
        if item not in self:
            super(TreeNodeContainer, self).append(item)
            complementary_items = getattr(item, self.complementary_items_name)
            complementary_items.append(self.owner)
    
    def remove(self, item):
        if item in self:
            super(TreeNodeContainer, self).remove(item)
            complementary_items = getattr(item, self.complementary_items_name)
            complementary_items.remove(self.owner)
