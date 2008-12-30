from abstract import AbstractContainer
from container import HorizontalContainer, VerticalContainer

def initialize_element_heights(elem, element_height): # test this!
    if isinstance(elem, VerticalContainer):
        elem.height = 0
        
        for child in elem.children:
            if isinstance(child, HorizontalContainer):
                child.height = child.find_child_max_height()
    elif isinstance(elem, HorizontalContainer):
        elem.height = 0
    elif not elem.height:
        elem.height = element_height
    
    if elem.children:
        heights = []
        for child in elem.children:
            height = initialize_element_heights(child, element_height)
            
            heights.append(height)
        
        if isinstance(elem, VerticalContainer):
            elem.height = sum(heights)
        else:
            elem.height += max(heights)
    
    return elem.height

def initialize_element_widths(elem): # test this!
    if elem.parent:
        if not elem.width:
            elem.width = elem.parent.width
        
        elem.width = min(elem.width, elem.parent.width)
        
        if isinstance(elem, HorizontalContainer):
            calculate_children_widths(elem, elem.children, elem.width)
    
    for child in elem.children:
        initialize_element_widths(child)

def calculate_children_widths(elem, children, width):
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