# -*- coding: utf-8 -*-
import sys
from bui.utils.math import clamp

ABSOLUTE = 'absolute'
RELATIVE = 'relative'
AUTO = 'auto'
MODES = (ABSOLUTE, RELATIVE, AUTO, )

class ConstrainedValueProperties(object):
    def get_width(self):
        return self._constrained_width.value
    def set_width(self, width):
        self._constrained_width.value = width
    width = property(get_width, set_width)
    
    def get_width_mode(self):
        return self._constrained_width.mode
    def set_width_mode(self, width_mode):
        self._constrained_width.mode = width_mode
    width_mode = property(get_width_mode, set_width_mode)
    
    def get_min_width(self):
        return self._constrained_width.min_value
    def set_min_width(self, min_width):
        self._constrained_width.min_value = min_width
    min_width = property(get_min_width, set_min_width)
    
    def get_max_width(self):
        return self._constrained_width.max_value
    def set_max_width(self, max_width):
        self._constrained_width.max_value = max_width
    max_width = property(get_max_width, set_max_width)
    
    def get_height(self):
        return self._constrained_height.value
    def set_height(self, height):
        self._constrained_height.value = height
    height = property(get_height, set_height)
    
    def get_height_mode(self):
        return self._constrained_height.mode
    def set_height_mode(self, height_mode):
        self._constrained_height.mode = height_mode
    height_mode = property(get_height_mode, set_height_mode)
    
    def get_min_height(self):
        return self._constrained_height.min_value
    def set_min_height(self, min_height):
        self._constrained_height.min_value = min_height
    min_height = property(get_min_height, set_min_height)
    
    def get_max_height(self):
        return self._constrained_height.max_value
    def set_max_height(self, max_height):
        self._constrained_height.max_value = max_height
    max_height = property(get_max_height, set_max_height)

class ConstrainedValue(object):
    def __init__(self, attribute_name, owner, mode, value, min_value, max_value):
        assert attribute_name in ('width', 'height', )
        assert mode in MODES
        assert 0 <= min_value <= max_value
        
        self.attribute_name = attribute_name
        self.owner = owner
        self._mode = mode
        self._value = value
        
        self.value = value
        self._min_value = min_value
        self._max_value = max_value
    
    def get_min_value(self):
        return self._min_value
    def set_min_value(self, min_value):
        assert 0 <= min_value <= self.max_value
        self._min_value = min_value
    min_value = property(get_min_value, set_min_value)
    
    def get_max_value(self):
        return self._max_value
    def set_max_value(self, max_value):
        assert self.min_value <= max_value
        self._max_value = max_value
    max_value = property(get_max_value, set_max_value)
    
    def get_mode(self):
        return self._mode
    def set_mode(self, mode):
        if mode in MODES:
            self._mode = mode
    mode = property(get_mode, set_mode)
    
    def get_value(self):
        if self.mode == ABSOLUTE:
            # cyclic dependency!
            from layout import FreeLayout
            if self.owner.parent and not isinstance(self.owner.parent, FreeLayout):
                parent_value = getattr(self.owner.parent, self.attribute_name)
                real_max = min(parent_value, self.max_value)
                return clamp(self._value, self.min_value, real_max)
        
        if self.mode == RELATIVE:
            if self.owner.parent:
                parent_value = getattr(self.owner.parent, self.attribute_name)
                # TODO: should clamp this to min/max?
                return parent_value * self._value / 100.0
        
        if self.mode == AUTO:
            default_value = self.owner.find_default_value(self.attribute_name)
            
            if default_value:
                parent_value = sys.maxint
                
                if self.owner.parent:
                    parent_value = getattr(self.owner.parent, self.attribute_name)
                
                return min(default_value, parent_value)
            
            # cyclic dependency!
            from layout import HorizontalLayout
            if self.owner.parent and not isinstance(self.owner.parent, HorizontalLayout):
                parent_value = getattr(self.owner.parent, self.attribute_name)
                return clamp(parent_value, self.min_value, self.max_value)
        
        # TODO: should clamp this to min/max?
        return self._value
    def set_value(self, value):
        self._value = value
    value = property(get_value, set_value)
    
    def __cmp__(self, other):
        return cmp(self.value, other)
    
    def __add__(self, other):
        return self.value + other
    
    def __iadd__(self, other):
        return self.__add__(self, other)
    
    def __radd__(self, other):
        return self.__add__(self, other)
    
    def __div__(self, other):
        return self.value / other
    
    def __idiv__(self, other):
        return self.__div__(other)
    
    def __rdiv__(self, other):
        return self.__div__(other)
    
    def __mul__(self, other):
        return self.value * other
    
    def __imul__(self, other):
        return self.__mul__(other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __sub__(self, other):
        return self.value - other
    
    def __isub__(self, other):
        return self.__sub__(other)
    
    def __rsub__(self, other):
        return self.__sub__(other)
