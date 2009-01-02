# -*- coding: utf-8 -*-
from bui.utils.coordinate import Coordinate

def test_create_empty_coordinate():
    coord = Coordinate()
    
    assert coord.x == 0
    assert coord.y == 0

def test_create_coordinate_with_values():
    coord = Coordinate(x=2.0, y=6.0)
    
    assert coord.x == 2.0
    assert coord.y == 6.0

def test_add_coordinates():
    coord1 = Coordinate(x=2.0, y=-4.0)
    coord2 = Coordinate(x=5.0, y=2.0)
    
    coord1 += coord2
    
    assert coord1.x == 7.0
    assert coord1.y == -2.0

def test_add_number_to_coordinate():
    coord = Coordinate(x=4.0, y=2.0)
    
    coord += 5.0
    
    assert coord.x == 9.0
    assert coord.y == 7.0
