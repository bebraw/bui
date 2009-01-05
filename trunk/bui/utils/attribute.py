# -*- coding: utf-8 -*-
from math import clamp

class AttributeSetter(object):
    def __setattr__(self, instance, value):
        if isinstance(value, Attribute):
            self.__dict__[instance] = value
        else:
            self_vars = vars(self)
            
            if self_vars.has_key(instance):
                attribute = self_vars[instance]
                
                if not hasattr(attribute, 'type'):
                    self.__dict__[instance] = value
                elif attribute.type is type(value):
                    attribute.value = value
                else:
                    raise TypeError, "Types of attribute and value assigned don't match!"
            else:
                self.__dict__[instance] = value

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
    def __init__(self, value):
        super(BooleanAttribute, self).__init__(value)
        self.type = bool

class IntegerAttribute(Attribute):
    def __init__(self, value, min, max):
        self.type = int
        
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
    
    #def __setattr__(self, instance, value):
    #    print instance, value

class StringAttribute(Attribute):
    def __init__(self, value):
        super(StringAttribute, self).__init__(value)
        self.type = str
