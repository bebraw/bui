# -*- coding: utf-8 -*-
from abstract import AbstractObject
from tree import TreeChild, TreeParent

class AbstractContainer(TreeChild, TreeParent, AbstractObject):
    def __init__(self, args=None):
        super(AbstractContainer, self).__init__(args)
        
        self.x_offset = 0
        self.y_offset = 0
    
    def has_only_container_children(self):
        if hasattr(self, 'children'):
            for child in self.children:
                return isinstance(child, AbstractContainer) # not right but works. this needs a proper test!
    
    def initialize_element_heights(self, element_height, elem=None):
        if elem is None:
            elem = self
        
        if not hasattr(elem, 'height'):
            elem.height = element_height
        
        if isinstance(elem, AbstractContainer) and elem.has_only_container_children():
            elem.height = 0
        
        if hasattr(self, 'children'):
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
        
        if hasattr(self, 'children'):
            if isinstance(elem, HorizontalContainer):
                calculate_children_widths(elem.children, elem.width)
            
            for child in elem.children:
                if isinstance(child, AbstractContainer):
                    child.initialize_element_widths(element_width, child)

class EmptyContainer(AbstractContainer):
    def render(self, coord):
        pass

class HorizontalContainer(AbstractContainer):
    def render(self, coord):
        tmp_x = coord.x
        
        for child in self.children:
            if child.visible:
                child.render(coord)
                coord.x += child.width
        
        coord.x = tmp_x

class VerticalContainer(AbstractContainer):
    def render(self, coord):
        coord.x += self.x_offset
        coord.y += self.y_offset
        
        for child in self.children:
            if child.visible:
                coord.y -= child.height
                child.render(coord)
