# -*- coding: utf-8 -*-
from abstract import AbstractContainer
from container import HorizontalContainer, VerticalContainer

class BaseLayoutManager(object):
    def __init__(self, window_manager, root_container, element_height):
        assert isinstance(root_container, AbstractContainer)
        assert isinstance(element_height, int)
        
        self.window_manager = window_manager
        self.element_height = element_height
        self.root_container = root_container
    
    def initialize_layout(self):
        self.initialize_element_heights(self.root_container)
        self.initialize_element_widths(self.root_container)
        self.initialize_coordinates()
    
    def initialize_coordinates(self):
        def initialize_coordinates_recursion(elem, coord, parent_is_visible=True):
            elem.x = coord.x
            elem.y = coord.y
            
            coord.x += elem.x_offset
            coord.y += elem.y_offset
            
            if not elem.visible:
                parent_is_visible = elem.visible
            
            if isinstance(elem, HorizontalContainer):
                tmp_x = coord.x
                
                for child in elem.children:
                    if child.visible:
                        tmp_y = None
                        
                        if isinstance(child, VerticalContainer):
                            tmp_y = coord.y
                        
                        initialize_coordinates_recursion(child, coord, parent_is_visible)
                        
                        coord.x += child.width
                        coord.y = tmp_y or coord.y
                
                coord.x = tmp_x
            
            if isinstance(elem, VerticalContainer):
                for child in elem.children:
                    initialize_coordinates_recursion(child, coord, parent_is_visible)
                    
                    if not isinstance(child, VerticalContainer):
                        coord.y += child.height
            
            if not parent_is_visible:
                elem.x = None
                elem.y = None
        
        coord = self.window_manager.get_initial_coordinates()
        initialize_coordinates_recursion(self.root_container, coord)
    
    def initialize_element_heights(self, elem, parent_is_visible=True):
        if not elem.visible:
            parent_is_visible = elem.visible
        
        if isinstance(elem, VerticalContainer):
            elem.height = 0
            
            for child in elem.children:
                if isinstance(child, HorizontalContainer):
                    child.height = child.find_child_max_height()
        elif isinstance(elem, HorizontalContainer):
            elem.height = 0
        
        if elem.children:
            heights = []
            for child in elem.children:
                height = self.initialize_element_heights(child, parent_is_visible)
                
                heights.append(height)
            
            if isinstance(elem, VerticalContainer):
                elem.height = sum(heights)
            else:
                elem.height += max(heights)
        
        if parent_is_visible:
            if not isinstance(elem, HorizontalContainer) and not isinstance(elem, VerticalContainer):
                elem.height = elem.height or self.element_height
        else:
            elem.height = 0
        
        return elem.height
    
    def initialize_element_widths(self, elem):
        if elem.parent:
            if not elem.width:
                elem.width = elem.parent.width
            
            elem.width = min(elem.width, elem.parent.width)
            
            if isinstance(elem, HorizontalContainer):
                self.calculate_children_widths(elem, elem.children, elem.width)
        
        for child in elem.children:
            self.initialize_element_widths(child)
    
    def calculate_children_widths(self, elem, children, width):
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
