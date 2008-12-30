# -*- coding: utf-8 -*-
from abstract import AbstractOpenGLElement

class Label(AbstractOpenGLElement):
    def render(self):
        super(Label, self).render()
        print 'render label' # use cairo + pango for this?
