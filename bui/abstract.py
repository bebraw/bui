# -*- coding: utf-8 -*-
from treehelper import TreeHelper

'''
TODO:
-clean up abstract classes (suitable_values, __init__)
'''

class AbstractObject(object):
    suitable_values = None
    
    def __init__(self, args=None):
        self.visible = True # is this on right abstraction level?
        
        super(AbstractObject, self).__init__(args)
        
        if type(args) is dict:
            for suitable_value in self.suitable_values:
                arg_value = self.check_arg(args, suitable_value)
                
                if arg_value is not None:
                    self.__dict__[suitable_value] = arg_value
    
    def __getattr__(self, name):
        return None
    
    def check_arg(self, dict, arg):
        if dict.has_key(arg):
            return dict[arg]
    
    def initialize_element_heights(self, element_height, elem=None):
        if elem is None:
            elem = self
        
        if elem.height is None:
            elem.height = element_height

        if isinstance(elem, AbstractContainer) and elem.has_only_container_children():
            elem.height = 0
        
        if elem.children:
            for child in elem.children:
                self.initialize_element_heights(element_height, child)

    def initialize_element_widths(self, element_width, elem=None):
        def calculate_children_widths(children, width):
            children_widths = len(children)*[None]
            width_left = width
            free_indices = []
            
            # TODO: doesn't handle predef-free-predef-free case yet? (should it?)
            for i, child in enumerate(children):
                children_widths[i] = child.width
                
                if child.width:
                    width_left -= child.width
                else:
                    free_indices.append(i)
            
            amount = len(free_indices)
            avg_per_child = width_left / amount if amount else 0
            extra_pixels = width_left - amount * avg_per_child
            
            for i, free_index in enumerate(free_indices):
                children_widths[free_index] = avg_per_child if i >= extra_pixels else avg_per_child + 1
            
            for i, child in enumerate(children):
                child.width = children_widths[i]
        
        if elem is None:
            elem = self
        
        if elem.width is None:
            elem.width = element_width
        
        if elem.children:
            if isinstance(elem, HorizontalContainer):
                calculate_children_widths(elem.children, elem.width)
            
            for child in elem.children:
                child.initialize_element_widths(element_width, child)

class AbstractContainer(AbstractObject, TreeHelper):
    suitable_values = ('name', 'visible', 'width', 'height', 'min_width', 'max_width', )
    
    def has_only_container_children(self):
        for child in self.children:
            return isinstance(child, AbstractContainer) # not right but works. this needs a proper test!

class AbstractElement(AbstractObject, TreeHelper):
    pass
