# -*- coding: utf-8 -*-

class Coordinate():
    def __init__(self, x, y):
        assert type(x) == int
        assert type(y) == int
        self.x = x
        self.y = y
    
    def inside(self, element):
        try:
            element_left_x = element.x
            element_right_x = element.x + element.width
            element_top_y = element.y
            element_bottom_y = element.y + element.height
            
            if element_left_x < self.x < element_right_x:
               if element_top_y < self.y < element_bottom_y:
                   return True
        except:
            pass
        
        return False
