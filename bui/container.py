# -*- coding: utf-8 -*-
from abstract import AbstractAttributes, AbstractObject
from serializer import unserialize
from tree import TreeChild, TreeParent

# IMPORTANT! This class needs to be here due to its dependency on HorizontalContainer!
# TODO: move this class to abstract and separate width/height inits to own file
class AbstractContainer(TreeChild, TreeParent, AbstractAttributes, AbstractObject):
    def __init__(self, args=None):
        self.x_offset = 0
        self.y_offset = 0
        super(AbstractContainer, self).__init__(args)
    
    def add_child_structure(self, structure, namespace):
        structure_root = unserialize(structure, namespace)
        structure_root.parent = self
        self.children.append(structure_root)
        
        return structure_root
    
    def has_only_container_children(self):
        if self.children:
            for child in self.children:
                if not isinstance(child, AbstractContainer):
                    return False
            
            return True
        
        return False
    
    def initialize_element_heights(self, element_height): # test this!
        def initialize_element_heights_recursion(element_height, elem):
            if not elem.height:
                elem.height = element_height
            
            if isinstance(elem, AbstractContainer) and elem.has_only_container_children():
                elem.height = 0
            
            for child in elem.children:
                initialize_element_heights_recursion(element_height, child)
        
        initialize_element_heights_recursion(element_height, self)
    
    def calculate_children_widths(self, children, width):
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
    
    def initialize_element_widths(self): # test this!
        if self.parent:
            if not self.width:
                self.width = self.parent.width
            
            self.width = min(self.width, self.parent.width)
            
            if isinstance(self, HorizontalContainer):
                self.calculate_children_widths(self.children, self.width)
        
        for child in self.children:
            if isinstance(child, AbstractContainer):
                child.initialize_element_widths()

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
