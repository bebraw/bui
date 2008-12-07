# -*- coding: utf-8 -*-

class AllMethodsStaticMetaclass(type):
    def __init__(cls, name, bases, dct):
        for func in dct.values():
            if hasattr(func, '__call__'):
                setattr(cls, func.__name__, staticmethod(func))                
        super(AllMethodsStaticMetaclass, cls).__init__(name, bases, dct)
 
class AllMethodsStatic(object):
    __metaclass__ = AllMethodsStaticMetaclass
