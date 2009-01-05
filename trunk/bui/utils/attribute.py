# -*- coding: utf-8 -*-
from math import clamp

class AttributeSetter(object):
    def __setattr__(self, instance, value):
        if isinstance(value, Attribute):
            self.__dict__[instance] = value
        else:
            if hasattr(instance, 'value'): # FIXME: a bit weak
                self.__dict__[instance].value = value
            else:
                self.__dict__[instance] = value

class AttributeFactory(object):
    pass

class Attribute(object):
    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        try:
            return self.value
        except:
            raise AttributeError, name

    def __cmp__(self, other):
        return cmp(self.value, other)

class BooleanAttribute(Attribute):
    pass

class IntegerAttribute(Attribute):
    def __init__(self, value, min, max):
        self._value = value
        self.min = min
        self._max = max
    
    def get_max(self):
        return max(self.min, self._max)
    def set_max(self, max):
        self._max = max
    max = property(get_max, set_max)
    
    def get_value(self):
        return clamp(self._value, self.min, self.max)
    def set_value(self, value):
        self._value = value
    value = property(get_value, set_value)
    
    def __getattr__(self, name):
        try:
            if self.max < self.value:
                return self.max
            return self.value
        except:
            raise AttributeError, name

class StringAttribute(Attribute):
    pass
