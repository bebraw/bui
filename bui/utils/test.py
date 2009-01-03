# -*- coding: utf-8 -*-

def raises(exception, exception_value, func):
    try:
        func()
    except Exception, e:
        if isinstance(e, exception):
            assert e.value == exception_value, 'Wrong exception value! Expected "%s" but got "%s" instead.' % (exception_value, e.value)
        else:
            # FIXME: it's possible that an exception is thrown during execution. should check this case separately!
            assert False, 'Wrong exception type! %s' % (repr(e), )
