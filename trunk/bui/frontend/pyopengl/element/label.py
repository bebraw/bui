# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject
from bui.graphics.opengl.font import Font

class Label(AbstractObject):
    def __init__(self, **kvargs):
        self.label = ''
        self.color = 3*[0.0]
        self.alpha = 1.0
        self.font_name = 'Vera'
        
        super(Label, self).__init__(**kvargs)
        
        self.font = Font(self.font_name)
    
    def render(self):
        self.font.render(self)
