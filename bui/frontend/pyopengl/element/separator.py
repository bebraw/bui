# -*- coding: utf-8 -*-
from bui.backend.container.horizontal import HorizontalContainer
from bui.backend.container.vertical import VerticalContainer
from bui.graphics.opengl.draw import draw_line
from abstract import AbstractOpenGLElement
from label import Label

class Separator(AbstractOpenGLElement):
    def initialize(self, **kvargs):
        self.color = 3*[0.0]
        self.alpha = 1.0
        self.font_name = 'Vera'
        
        super(Separator, self).initialize(**kvargs)
        
        self.label = Label()
        self.label.initialize(**kvargs)
        
        self.label.x = 100
        self.label.x_is_relative = False
    
    def render(self):
        super(Separator, self).render()
        
        text_sep_dist = 10
        
        if isinstance(self.parent, HorizontalContainer):
            x_coord = self.x + self.width / 2.0
            
            # TODO: implement name rendering (should rotate Draw.Text somehow?)
            draw_line(0.5, self.color, x_coord, self.y, x_coord, self.y + self.height)
        
        if isinstance(self.parent, VerticalContainer):
            y_coord = self.y + self.height / 2.0
            
            bbox = self.label.font.get_bounding_box()
            text_width = bbox.width
            
            text_x = self.x + (self.width - text_width) / 2.0
            
            sep_begin_x = self.x
            sep_end_x = max(sep_begin_x, text_x - text_sep_dist)
            draw_line(0.5, self.color, sep_begin_x, y_coord, sep_end_x, y_coord)
            
            text_y= y_coord - 5 # 5 = half of text height
            
            self.label.x = text_x
            self.label.y = text_y
            
            self.label.render()
            
            sep_end_x = self.x + self.width
            sep_begin_x = min(sep_end_x, text_x + text_width + text_sep_dist)
            draw_line(0.5, self.color, sep_begin_x, y_coord, sep_end_x, y_coord)
