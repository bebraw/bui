# -*- coding: utf-8 -*-
from Blender import Draw

from bui.application import Application

from bui.blender.event import BlenderEventManager
from bui.blender.window import BlenderWindowManager

class BlenderApplication(Application):
    def __init__(self, structure, keys, events=None, constraints=None, element_height=20):
        super(BlenderApplication, self).__init__(structure, keys, events, constraints, element_height)
        
        self.event_manager = BlenderEventManager(self.root_container, keys, events, element_height)
        self.window_manager = BlenderWindowManager()
    
    def run(self):
        Draw.Register(self._gui, self.event_manager.key_event, self.event_manager.element_event)
