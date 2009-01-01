# -*- coding: utf-8 -*-
from bui.graphics.opengl.font import Font
from abstract import AbstractOpenGLElement

class Label(AbstractOpenGLElement):
    def initialize(self, **kvargs):
        self.color = 3*[0.0]
        self.alpha = 1.0
        self.font_name = 'Vera'
        
        super(Label, self).initialize(**kvargs)
        
        self.font = Font(self)
    
    def render(self):
        self.font.render()
