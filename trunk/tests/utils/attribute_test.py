# -*- coding: utf-8 -*-
from bui.utils.attribute import AttributeSetter, BooleanAttribute, IntegerAttribute, StringAttribute

class BooleanClass(AttributeSetter):
    def __init__(self):
        self.show_fps = BooleanAttribute(value=True)
        self.show_fps = False
        
        self.start_timers = BooleanAttribute(value=False)

def test_boolean_attribute():
    boolean_class = BooleanClass()
    assert boolean_class.show_fps == False
    
    assert boolean_class.start_timers == False
    
    #this should raise an exception (invalid type or something like that)
    #boolean_class.start_timers = 'cat'

class IntegerClass(AttributeSetter):
    def __init__(self):
        self.age = IntegerAttribute(value=5, min=2, max=40)
        self.age = 12
        
        self.width = IntegerAttribute(value=80, min=1, max=50)
        self.height = IntegerAttribute(value=-100, min=10, max=60)
        
        self.min_bigger_than_max = IntegerAttribute(value=5, min=100, max=1)

def test_integer_attribute():
    integer_class = IntegerClass()
    assert integer_class.age == 12, setter.age
    assert integer_class.age.min == 2, setter.age.min
    assert integer_class.age.max == 40, setter.age.max
    
    assert integer_class.width == 50
    assert integer_class.width.min == 1
    assert integer_class.width.max == 50
    
    assert integer_class.height == 10
    assert integer_class.height.min == 10
    assert integer_class.height.max == 60
    
    # if min > max, use min as max (could use some other convention too)
    # should it give a warning about this case?
    assert integer_class.min_bigger_than_max == 100
    assert integer_class.min_bigger_than_max.min == 100
    assert integer_class.min_bigger_than_max.max == 100
    
class StringClass(AttributeSetter):
    def __init__(self):
        self.name = StringAttribute(value='John')
        self.name = 'Jack'
        
        self.surname = StringAttribute(value='Doe')

def test_string_attribute():
    string_class = StringClass()
    assert string_class.name == 'Jack'
    
    assert string_class.surname == 'Doe'

# TODO: add exceptional cases (type checking!)
# TODO: add messages for exceptions
# TODO: add factory (handles base message and constructs attributes)
