# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractNode
from bui.backend.layout import *
from bui.graphics.opengl.draw import draw_line
from bui.graphics.opengl.font import Font

class Label(AbstractNode):
    def __init__(self, **kvargs):
        self.label = ''
        self.color = 3*[0.0]
        self.alpha = 1.0
        self.font_name = 'Vera'
        
        super(Label, self).__init__(**kvargs)
        
        self.font = Font(self.font_name)
    
    def render(self):
        self.font.render(self)

# would it make sense just to inherit label instead???
class Separator(AbstractNode):
    def __init__(self, **kvargs):
        self.label = ''
        self.color = 3*[0.0]
        self.alpha = 1.0
        self.font_name = 'Vera'
        
        super(Separator, self).__init__(**kvargs)
        
        self.text_label = Label(**kvargs)
    
    def render(self):
        line_width = 0.5
        text_sep_dist = 10
        
        if isinstance(self.parent, HorizontalLayout):
            x_coord = self.x + self.width / 2.0
            
            # TODO: implement name rendering (should rotate Draw.Text somehow?)
            draw_line(0.5, self.color, x_coord, self.y, x_coord, self.y + self.height)
        
        if isinstance(self.parent, VerticalLayout):
            y_coord = self.y + self.height / 2.0
            
            self.text_label.height = self.height # XXX: without this draw_line starts to complain
            
            bbox = self.text_label.font.get_bounding_box(self.text_label)
            text_width = bbox.width
            
            text_x = self.x + (self.width - text_width) / 2.0
            
            sep_begin_x = self.x
            sep_end_x = max(sep_begin_x, text_x - text_sep_dist)
            draw_line(line_width, self.color, sep_begin_x, y_coord, sep_end_x, y_coord)
            
            text_y= y_coord - bbox.height / 2.0
            
            self.text_label.x = text_x
            self.text_label.y = text_y
            
            self.text_label.render()
            
            sep_end_x = self.x + self.width
            sep_begin_x = min(sep_end_x, text_x + text_width + text_sep_dist)
            draw_line(line_width, self.color, sep_begin_x, y_coord, sep_end_x, y_coord)
