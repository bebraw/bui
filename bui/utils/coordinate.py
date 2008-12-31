# -*- coding: utf-8 -*-

class Coordinate():
    def __init__(self, x=0, y=0):
        assert type(x) in (float, int)
        assert type(y) in (float, int)
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
