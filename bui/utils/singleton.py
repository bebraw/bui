# -*- coding: utf-8 -*-

class Singleton(object):
    ''' http://code.activestate.com/recipes/66531/ '''
    def __new__(cls, *p, **k):
        if not '_the_instance' in cls.__dict__:
            cls._the_instance = object.__new__(cls)
        return cls._the_instance
