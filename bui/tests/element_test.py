# -*- coding: utf-8 -*-
from bui.element import EmptyElement

def test_empty_element():
    empty_element = EmptyElement(width=200)
    
    assert isinstance(empty_element, EmptyElement)
    assert empty_element.width == 200
