# -*- coding: utf-8 -*-

# TODO: make more generic??? x,y,z,w???

class Coordinate():
    def __init__(self, x=0, y=0):
        assert type(x) in (float, int)
        assert type(y) in (float, int)
        self.x = x
        self.y = y
    
    def __add__(self, fac):
        if isinstance(fac, Coordinate):
            return Coordinate(x=self.x + fac.x, y=self.y + fac.y)
        if type(fac) in (float, int):
            return Coordinate(x=self.x + fac, y=self.y + fac)
    
    # TODO: test! (move outside???)
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
