# -*- coding: utf-8 -*-

# TODO: convert doc test to unit test
def clamp(n, min_val, max_val):
    '''
    >>> a = 1.0; b = 2.0; c = 3.0
    >>> clamp(a, b, c)
    2.0
    >>> clamp(c, a, b)
    2.0
    >>> clamp(b, a, c)
    2.0
    '''
    n = max(n, min_val)
    n = min(n, max_val)
    return n
