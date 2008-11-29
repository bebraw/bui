# -*- coding: utf-8 -*-
from Blender import Window
from Blender.Window import Types

from bui.event import EventManager

from keys import BLENDER_KEYS

class BlenderEventManager(EventManager):
    def __init__(self, root_container, keys, events, element_height):
        super(BlenderEventManager, self).__init__(root_container, keys, events, element_height)
    
    def element_event(self, evt):
        super(BlenderEventManager, self).element_event(evt)
        
        Window.Redraw(Types.VIEW3D) # TODO: too specific?
        Window.Redraw(Types.SCRIPT)
    
    def construct_key_event_ids(self, keys, key_mapping=None):
        super(BlenderEventManager, self).construct_key_event_ids(keys, BLENDER_KEYS)
