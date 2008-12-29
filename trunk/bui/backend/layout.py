# -*- coding: utf-8 -*-
from bui.utils.coordinate import Coordinate

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
        # FIXME: trigger width initializing (kludge). the problem is that widths cannot be
        # cascaded until the structure has been fully constructed (causes issues in setters too).
        # it would probably make sense to delay setting of widths in construction phase (cascade
        # only after child-parent relations have been formed)
        self.root_container.width = self.root_container.width
        self.initialize_coordinates()
    
    def initialize_coordinates(self, coord=None):
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
        
        coord = coord or Coordinate()
        
        initialize_coordinates_recursion(self.root_container, coord)
    
    # cascade heights!
    def initialize_element_heights(self, elem):
        if isinstance(elem, AbstractContainer):
            elem.height = 0
        
        if isinstance(elem, VerticalContainer):
            for child in elem.children:
                if isinstance(child, HorizontalContainer):
                    child.height = child.find_child_max_height()
        
        if elem.children:
            heights = []
            for child in elem.children:
                height = self.initialize_element_heights(child)
                
                heights.append(height)
            
            if isinstance(elem, VerticalContainer):
                elem.height = sum(heights)
            else:
                elem.height += max(heights)
        
        if not isinstance(elem, AbstractContainer):
            elem.height = elem.height or self.element_height
        
        return elem.height
