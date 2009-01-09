# -*- coding: utf-8 -*-
import sys
from bui.utils.math import clamp

ABSOLUTE = 'absolute'
RELATIVE = 'relative'
AUTO = 'auto'
MODES = (ABSOLUTE, RELATIVE, AUTO, )

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
