# -*- coding: utf-8 -*-
from Blender import Window
from Blender.Window import Types

from bui.event import BaseEventManager

from keys import BLENDER_KEYS

class EventManager(BaseEventManager):
    def __init__(self, root_container, keys, events):
        super(EventManager, self).__init__(root_container, keys, events)
    
    def element_event(self, evt):
        super(EventManager, self).element_event(evt)
        
        Window.Redraw(Types.VIEW3D) # TODO: too specific?
        Window.Redraw(Types.SCRIPT)
    
    def construct_key_event_ids(self, keys, key_mapping=None):
        super(EventManager, self).construct_key_event_ids(keys, BLENDER_KEYS)
