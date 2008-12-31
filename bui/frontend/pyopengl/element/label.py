# -*- coding: utf-8 -*-
from __future__ import with_statement

# TODO: clean up!
from OpenGL.GL import glPopMatrix, glPushMatrix

# set drawing functions to use Blender's OpenGL implementation
# TODO: tidy up (get rid of ogl and just dump whole namespace into draw?)
import OpenGL.GL
import bui.graphics.opengl.decorators
import bui.graphics.opengl.matrix_stack
import bui.graphics.opengl.setters
import bui.graphics.opengl.transformations
setattr(bui.graphics.opengl.decorators, 'ogl', OpenGL.GL)
setattr(bui.graphics.opengl.matrix_stack, 'ogl', OpenGL.GL)
setattr(bui.graphics.opengl.setters, 'ogl', OpenGL.GL)
setattr(bui.graphics.opengl.transformations, 'ogl', OpenGL.GL)

from bui.graphics.opengl.decorators import enable_alpha, enable_texture2d
from bui.graphics.opengl.matrix_stack import MatrixStack
from bui.graphics.opengl.setters import set_color
from bui.graphics.opengl.transformations import mirror_y, translate

from bui.utils.font import Font

from abstract import AbstractOpenGLElement

class Label(AbstractOpenGLElement):
    def initialize(self, **kvargs):
        self.color = 3*[0.0]
        self.alpha = 1.0
        self.font_name = 'Vera'
        super(Label, self).initialize(**kvargs)
        
        self.font = Font(self.font_name)
    
    @enable_alpha
    @enable_texture2d
    def render(self):
        super(Label, self).render()
        
        set_color(self.color, alpha=self.alpha)
        
        with MatrixStack():
            # note that FTGL uses OpenGL drawing convention by default!
            translate(self.x, self.y + self.height)
            mirror_y()
            
            self.font.render(self.name, self.height)
