# -*- coding: utf-8 -*-
from bui.graphics.opengl.font import Font
from abstract import AbstractOpenGLElement

class Label(AbstractOpenGLElement):
    def __init__(self, **kvargs):
        self.color = 3*[0.0]
        self.alpha = 1.0
        self.font_name = 'Vera'
        super(Label, self).__init__(**kvargs)
        self.font = Font(self)
    
    def render(self):
        super(Label, self).render()
        self.font.render()
