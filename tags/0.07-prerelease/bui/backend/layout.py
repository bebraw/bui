# -*- coding: utf-8 -*-
from abstract import AbstractNode

class Layout(AbstractNode):
    def __init__(self, **kvargs):
        self.default_node_width = 0
        self.default_node_height = 0
        # TODO: add default_node_color here (add getter to use color of parent just like in case of width/height (same logic))
        super(Layout, self).__init__(**kvargs)
    
    def append(self, item):
        self.children.append(item)
    
    def remove(self, item):
        self.children.remove(item)
    
    def render_child(self, child, render_coordinate):
        if child.visible:
            if isinstance(child, Layout):
                render_coordinate = child.render(render_coordinate)
            else:
                child.x = render_coordinate.x
                child.y = render_coordinate.y
                child.render_bg_color(render_coordinate)
                child.render()
        
        return render_coordinate

class FreeLayout(Layout):
    def render(self, render_coordinate=None):
        render_coordinate = super(Layout, self).render(render_coordinate)
        
        for child in self.children:
            self.render_child(child, render_coordinate=None)
        
        return render_coordinate

class HorizontalLayout(Layout):
    def render(self, render_coordinate=None):
        render_coordinate = super(Layout, self).render(render_coordinate)
        
        tmp_x = render_coordinate.x
        
        # FIXME: doesn't take children modes in count!
        # this means that it calculates correctly only on first time! (after that width is set!)
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
    
    # TODO: should generalize this and use for both vertical/horizontal layout!
    # TODO: make this dynamic and take children modes in count!
    def _calculate_children_widths(self):
        children_widths = len(self.children)*[None]
        width_left = self.width
        free_indices = []
        
        for i, child in enumerate(self.children):
            children_widths[i] = child.width
            
            if child.width:
                width_left -= child.width
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

class VerticalLayout(Layout):
    def render(self, render_coordinate=None):
        render_coordinate = super(Layout, self).render(render_coordinate)
        
        # XXX: calculate children heights
        # self._calculate_children_heights()
        
        for child in self.children:
            render_coordinate = self.render_child(child, render_coordinate)
            
            render_coordinate.y += child.height
        
        return render_coordinate
