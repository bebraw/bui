# -*- coding: utf-8 -*-
import os
import Blender
from Blender import Draw
from bui.graphics.opengl.decorators import enable_alpha
from abstract import AbstractBlenderElement
from utils import change_extension, convert_svg_to_png, find_file_path, get_icons_dir, \
                  load_image

class Image(AbstractBlenderElement):
    def initialize(self, **kvargs):
        self.dir = Blender.Get('uscriptsdir')
        self.file = ''
        self.x_zoom = 1.0
        self.y_zoom = 1.0
        self.x_clip = 0
        self.y_clip = 0
        self.clip_width = -1
        self.clip_height = -1
        self.image_block = None
        super(Image, self).initialize(**kvargs)
        
        # TODO: it would be safer to check the file header
        if self.file.endswith('svg'):
            self.dir = get_icons_dir()
            
            source_dir = Blender.Get('uscriptsdir')
            svg_path = find_file_path(source_dir, self.file)
            
            png_name = change_extension(self.file, 'png')
            png_path = os.path.join(self.dir, png_name)
            
            convert_svg_to_png(svg_path, png_path, self.width, self.height)
            
            self.file = png_name # use png version from now on
        
        self.image_block = load_image(self.dir, self.file)
        self.set_element_dimensions()
    
    def set_element_dimensions(self):
        if self.image_block:
            width, height = self.image_block.getSize()
            
            if self.height and self.width:
                self.height = self.height
                self.width = self.width
            elif self.height:
                self.height = self.height
                self.width = float(self.height) / height * width
            elif self.width:
                self.height = float(self.width) / width * height
                self.width = self.width
            else:
                self.height = height
                self.width = width
    
    @enable_alpha
    def render(self):
        if self.image_block:
            width, height = self.image_block.getSize()
            self.x_zoom = float(self.width) / width
            self.y_zoom = float(self.height) / height
            
            Draw.Image(self.image_block, self.x, self.y,
                       self.x_zoom, self.y_zoom, self.x_clip, self.y_clip,
                       self.clip_width, self.clip_height)
