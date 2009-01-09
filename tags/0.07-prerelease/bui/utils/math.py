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

# TODO: generalize and test
def lerp(n, m, fac):
    ''' linear interpolation '''
    assert 0.0 <= fac <= 1.0, 'Got %f!' % fac
    
    # list version
    n_part = [i*(fac) for i in n]
    m_part = [i*(1-fac) for i in m]
    return [i+j for i, j in zip(n_part, m_part)]
    
    # nominal case
    #return n*fac + m*(1-fac)

# TODO: add other interpolation types
