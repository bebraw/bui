# -*- coding: utf-8 -*-
import Blender
from Blender import Draw

# FIXME: bound in right place? see image.py too!
import bui.graphics.opengl.decorators
setattr(bui.graphics.opengl.decorators, 'ogl', Blender.BGL)

from bui.graphics.opengl.decorators import enable_alpha

from abstract import AbstractBlenderElement
from icons import BLENDER_ICONS
from utils import load_image

class Icon(AbstractBlenderElement):
    def __init__(self, **kvargs):
        """ Adapted from txtPyBrowser114j.py by Remigiusz Fiedler """
        def get_icon_position(index):
            row = index / 25
            col = index - (row * 25)
            return row, col
        
        self.file = 'blenderbuttons.png'
        super(Icon, self).__init__(**kvargs)
        
        index = BLENDER_ICONS.index(self.name)
        row, col = get_icon_position(index)
        self.width = 20
        self.height = 21
        self.clip_x = col * self.width + 3
        self.clip_y = row * self.height + 3
        self.clip_width = 15
        self.clip_height = 15
        
        uscriptsdir = Blender.Get('uscriptsdir')
        self.image_block = load_image(uscriptsdir, self.file)
    
    @enable_alpha
    def render(self):
        Draw.Image(self.image_block, self.x, self.y, 1.0, 1.0, self.clip_x,
                   self.clip_y, self.clip_width, self.clip_height)
