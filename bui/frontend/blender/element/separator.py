# -*- coding: utf-8 -*-
import Blender
from Blender import Draw

# right place for binding? (should probably use separate func for this)
import bui.graphics.opengl.draw
setattr(bui.graphics.opengl.draw, 'ogl', Blender.BGL)

from bui.graphics.opengl.draw import draw_line

from abstract import AbstractBlenderElement
from utils import draw_text

class Separator(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.color = 3*[0.0]
        super(Separator, self).__init__(**kvargs)
    
    def render(self):
        text_sep_dist = 10
        
        if isinstance(self.parent, HorizontalContainer):
            x_coord = self.x + self.width / 2.0
            
            # TODO: implement name rendering (should rotate Draw.Text somehow?)
            draw_line(0.5, self.color, x_coord, self.y, x_coord, self.y + self.height)
        
        if isinstance(self.parent, VerticalContainer):
            y_coord = self.y + self.height / 2.0
            
            # HACK! draw text in some not visible place to get its width (needed for centering)
            text_width = draw_text(self.name, -10000.0, -10000.0)
            
            text_x = self.x + (self.width - text_width) / 2.0
            
            sep_begin_x = self.x
            sep_end_x = max(sep_begin_x, text_x - text_sep_dist)
            draw_line(0.5, self.color, sep_begin_x, y_coord, sep_end_x, y_coord)
            
            text_y= y_coord - 5 # 5 = half of text height
            draw_text(self.name, text_x, text_y)
            
            sep_end_x = self.x + self.width
            sep_begin_x = min(sep_end_x, text_x + text_width + text_sep_dist)
            draw_line(0.5, self.color, sep_begin_x, y_coord, sep_end_x, y_coord)
