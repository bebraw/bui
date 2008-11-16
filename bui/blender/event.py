# -*- coding: utf-8 -*-
from Blender import Window
from Blender.Window import Types

from bui.event import EventManager
from bui.parser import read_yaml

from keys import BLENDER_KEYS

class BlenderEventManager(EventManager):
    def __init__(self, root_container, keys, namespace, element_height):
        super(BlenderEventManager, self).__init__(root_container, keys, namespace, element_height)
    
    def element_event(self, evt):
        super(BlenderEventManager, self).element_event(evt)
        
        Window.Redraw(Types.VIEW3D) # TODO: too specific?
        Window.Redraw(Types.SCRIPT)
    
    def _construct_key_event_ids(self, keys, key_mapping=None):
        super(BlenderEventManager, self)._construct_key_event_ids(keys, BLENDER_KEYS)
        '''
        keys_structure = read_yaml(keys)
        
        if isinstance(keys_structure, dict):
            for key, func_name in keys_structure.items():
                if self.namespace.has_key(func_name):
                    blender_key = BLENDER_KEYS[key]
                    self.key_events[blender_key] = self.namespace[func_name]
        '''
