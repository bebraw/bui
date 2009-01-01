# -*- coding: utf-8 -*-
from abstract import AbstractLayout, AbstractObject

class HorizontalLayout(AbstractLayout):
    def get_height(self):
        record_height = self._find_child_max_height()
        
        if record_height > self._height:
            return record_height
        return self._height
    height = property(get_height, AbstractLayout.set_height)
    
    # TODO: add a test case for this
    def _find_child_max_height(self):
        record_height = 0
        
        for child in self.children:
            record_height = max(record_height, child.height)
        
        return record_height
    
    def set_width(self, width):
        super(HorizontalLayout, self).set_width(width)
        
        self._calculate_children_widths()
    width = property(AbstractObject.get_width, set_width)
    
    # TODO: add a test case for this (via set_width)
    def _calculate_children_widths(self):
        children_widths = len(self.children)*[None]
        width_left = self.width
        free_indices = []
        
        # TODO: doesn't handle predef-free-predef-free case yet? (should it?)
        for i, child in enumerate(self.children):
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
        
        for i, child in enumerate(self.children):
            child.width = children_widths[i]
    
    def render(self):
        super(HorizontalLayout, self).render()
        
        tmp_x = self.common.render_coordinate.x
        
        for child in self.children:
            tmp_y = None
            
            if isinstance(child, VerticalLayout):
                tmp_y = self.common.render_coordinate.y
            
            if child.visible:
                child.render()
            
            self.common.render_coordinate.x += child.width
            self.common.render_coordinate.y = tmp_y or self.common.render_coordinate.y
        
        self.common.render_coordinate.x = tmp_x

class VerticalLayout(AbstractLayout):
    def get_height(self):
        if self.visible:
            # TODO: make it possible to determine height explicitly (-> scrollbar)
            self._height = 0
            
            heights = []
            for child in self.children:
                if child.visible and child.height:
                    heights.append(child.height)
            
            self._height = sum(heights)
        
        return super(AbstractLayout, self).get_height()
    height = property(get_height, AbstractObject.set_height)
    
    def render(self):
        super(VerticalLayout, self).render()
        
        for child in self.children:
            if child.visible:
                child.render()
            
            if not isinstance(child, VerticalLayout):
                self.common.render_coordinate.y += child.height