# -*- coding: utf-8 -*-
from Blender import Window

from bui.coordinate import Coordinate
from bui.window import BaseWindowManager

class WindowManager(BaseWindowManager):
    def get_coordinates(self):
        win_id = Window.GetAreaID()
        win_data = Window.GetScreenInfo()
        
        for win in win_data:
            if win["id"] == win_id:
                return win["vertices"]
    
    def get_mouse_coordinates(self):
        xmin, ymin, xmax, ymax = self.get_coordinates()
        mouse_x, mouse_y = Window.GetMouseCoords()
        
        return Coordinate(mouse_x-xmin, ymax-mouse_y+ymin)
