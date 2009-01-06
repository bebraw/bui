# -*- coding: utf-8 -*-
from abstract import AbstractLayout
from render import RenderNode

class LayoutNode(RenderNode):
    def __init__(self, **kvargs):
        self._element_height = None
        super(LayoutNode, self).__init__(**kvargs)
    
    def get_element_height(self):
        if self.parent:
            return min(self.parent.height, self._element_height)
        
        if hasattr(self, '_element_height'):
            return min(self._height, self._element_height)
        
        return None
    def set_element_height(self, element_height):
        self._element_height = element_height
    element_height = property(get_element_height, set_element_height)
    
    def render_child(self, child, render_coordinate):
        if child.visible:
            if isinstance(child, AbstractLayout):
                render_coordinate = child.render(render_coordinate)
            else:
                child.x = render_coordinate.x
                child.y = render_coordinate.y
                child.render_bg_color(render_coordinate)
                child.render()
        
        return render_coordinate

class FreeLayout(AbstractLayout):
    def __init__(self, **kvargs):
        self.render_node = FreeLayoutNode(**kvargs)
        super(FreeLayout, self).__init__(**kvargs)

class FreeLayoutNode(LayoutNode):
    def render(self, render_coordinate=None):
        render_coordinate = super(FreeLayoutNode, self).render(render_coordinate)
        
        for child in self.children:
            self.render_child(child, render_coordinate=None)
        
        return render_coordinate

class HorizontalLayout(AbstractLayout):
    def __init__(self, **kvargs):
        self.render_node = HorizontalLayoutNode(**kvargs)
        super(HorizontalLayout, self).__init__(**kvargs)

class HorizontalLayoutNode(LayoutNode):
    def render(self, render_coordinate=None):
        render_coordinate = super(HorizontalLayoutNode, self).render(render_coordinate)
        
        tmp_x = render_coordinate.x
        
        self._calculate_children_widths()
        
        for child in self.children:
            tmp_y = None
            
            if isinstance(child, VerticalLayout):
                tmp_y = render_coordinate.y
            
            render_coordinate = self.render_child(child, render_coordinate)
            
            render_coordinate.x += child.width
            render_coordinate.y = tmp_y or render_coordinate.y
        
        render_coordinate.x = tmp_x
        
        return render_coordinate
    
    def _calculate_children_widths(self):
        children_widths = len(self.children)*[None]
        width_left = self.width
        free_indices = []
        
        # XXX: _ notation needed??? (goes past property!!!)
        for i, child in enumerate(self.children):
            children_widths[i] = child._width
            
            if child._width:
                width_left -= child._width
            else:
                free_indices.append(i)
        
        amount = len(free_indices)
        avg_per_child = width_left / amount if amount else 0
        extra_pixels = width_left - amount * avg_per_child
        
        # disperse extra pixels
        for i, free_index in enumerate(free_indices):
            if i >= extra_pixels:            
                children_widths[free_index] = avg_per_child
            else: 
                children_widths[free_index] = avg_per_child + 1
        
        # assign new widths
        for i, child in enumerate(self.children):
            child.width = children_widths[i]
    
    def get_height(self):
        return self._height or self._find_child_max_height()
    height = property(get_height, LayoutNode.set_height)
    
    def _find_child_max_height(self):
        record_height = 0
        
        for child in self.children:
            record_height = max(record_height, child.height)
        
        return record_height

class VerticalLayout(AbstractLayout):
    def __init__(self, **kvargs):
        self.render_node = VerticalLayoutNode(**kvargs)
        super(VerticalLayout, self).__init__(**kvargs)

class VerticalLayoutNode(LayoutNode):
    def render(self, render_coordinate=None):
        render_coordinate = super(VerticalLayoutNode, self).render(render_coordinate)
        
        for child in self.children:
            render_coordinate = self.render_child(child, render_coordinate)
            
            #if not isinstance(child, VerticalLayout):
            render_coordinate.y += child.height
        
        return render_coordinate
    
    def get_height(self):
        if self.visible:
            heights = []
            
            element_height = self.find_element_height() or 0
            
            for child in self.children:
                if child.visible:
                    heights.append(child.height or element_height)
            
            return sum(heights)
        
        return super(LayoutNode, self).get_height()
    height = property(get_height, LayoutNode.set_height)
