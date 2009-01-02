# -*- coding: utf-8 -*-
from OpenGL.GL import glDisable, glOrtho, GL_DEPTH_TEST
from bui.graphics.opengl.matrix import load_identity_matrix, set_matrix_mode, MODELVIEW, PROJECTION
from bui.graphics.opengl.transformations import translate
from bui.graphics.opengl.viewport import viewport

# TODO: generalize a bit further? (viewports!)
# TODO: wrap more OGL calls?
def setup_2D_projection(width, height):
    ''' Adapted from http://basic4gl.wikispaces.com/2D+Drawing+in+OpenGL '''
    set_matrix_mode(PROJECTION)
    load_identity_matrix()
    viewport(0, 0, width, height)
    
    glOrtho(0, width, height, 0, 0, 1)
    glDisable(GL_DEPTH_TEST)
    
    set_matrix_mode(MODELVIEW)
    load_identity_matrix()
    
    # Displacement trick for exact pixelization
    translate(x=0.375, y=0.375)
