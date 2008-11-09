# -*- coding: utf-8 -*-
from Blender import Window
from Blender.Window import Types

from bui.event import EventManager

# TODO: need to handle mapping between blender keycodes and generic ones!

class BlenderEventManager(EventManager):
    def __init__(self, root_container, keys, namespace, element_height):
        super(BlenderEventManager, self).__init__(root_container, keys, namespace, element_height)
    
    def element_event(self, evt):
        super(BlenderEventManager, self).element_event(evt)
        
        Window.Redraw(Types.VIEW3D) # TODO: too specific?
        Window.Redraw(Types.SCRIPT)
