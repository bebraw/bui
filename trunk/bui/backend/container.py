# -*- coding: utf-8 -*-
from abstract import AbstractContainer, AbstractObject

class HorizontalContainer(AbstractContainer):
    def get_height(self):
        record_height = self._find_child_max_height()
        
        if record_height > self._height:
            return record_height
        return self._height
    height = property(get_height, AbstractContainer.set_height)
    
    # TODO: should check children recursively! (vcontainer inside vcontainer etc.)
    # add a test case for this
    def _find_child_max_height(self):
        record_height = 0
        
        if hasattr(self, 'children'):
            for child in self.children:
                record_height = max(record_height, child.height)
        
        return record_height
    
    def set_width(self, width):
        super(HorizontalContainer, self).set_width(width)
        
        if hasattr(self, 'children'):
            self._calculate_children_widths()
    width = property(AbstractObject.get_width, set_width)
    
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

class VerticalContainer(AbstractContainer):
    def get_height(self):
        if self.visible:
            # TODO: make it possible to determine height explicitly (-> scrollbar)
            self._height = 0
            
            if hasattr(self, 'children'):
                heights = []
                for child in self.children:
                    if child.visible and child.height:
                        heights.append(child.height)
                
                self._height = sum(heights)
        
        return super(AbstractContainer, self).get_height()
    height = property(get_height, AbstractObject.set_height)
    
    def set_width(self, width):
        self._width = max(width, 0)
        
        if hasattr(self, 'children'):
            for child in self.children:
                child.width = self.width
        
        super(AbstractContainer, self).set_width(width)
    width = property(AbstractContainer.get_width, set_width)
