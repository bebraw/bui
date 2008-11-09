# -*- coding: utf-8 -*-
from Blender import Window
from Blender.Window import Types

from bui.event import EventManager

class BlenderEventManager(EventManager):
    def __init__(self, root_container, namespace, element_height):
        super(BlenderEventManager, self).__init__(root_container, namespace, element_height)
    
    def button_event(self, evt):
        super(BlenderEventManager, self).__init__(evt)
        
        Window.Redraw(Types.VIEW3D) # TODO: too specific?
        Window.Redraw(Types.SCRIPT)
