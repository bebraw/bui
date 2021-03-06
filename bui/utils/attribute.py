# -*- coding: utf-8 -*-

def set_attributes_based_on_kvargs(instance, excluded_attributes=None, **kvargs):
    ''' adapted from http://blog.enterthefoo.com/2008/08/pythons-vars.html '''
    for name in ( n for n in dir(instance) if n[0] != '_' ):
        attr = getattr(instance, name)
        
        if not callable(attr) and name in kvargs:
            if name not in excluded_attributes:
                setattr(instance, name, kvargs[name])
