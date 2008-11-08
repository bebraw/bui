# -*- coding: utf-8 -*-
from Blender import Draw

from bui.application import Application
from bui.blender.event import BlenderEventManager

'''
TODO:
-handle some Blender related namespace stuff (imports!)
'''

class BlenderApplication(Application):
    def __init__(self, structure, element_height=20):
        super(BlenderApplication, self).__init__(structure, element_height)
        
        self.event_manager = BlenderEventManager(self.root_container, element_height)
    
    def run(self):
        Draw.Register(self._gui, self.event_manager.event, self.event_manager.element_event)
