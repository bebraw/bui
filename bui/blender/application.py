# -*- coding: utf-8 -*-
from Blender import Draw

from bui.application import BaseApplication

from bui.blender.event import EventManager
from bui.blender.window import WindowManager

class Application(BaseApplication):
    def __init__(self, structure, keys, events=None, constraints=None, element_height=20):
        super(Application, self).__init__(structure, keys, events, constraints, element_height)
        
        self.event_manager = EventManager(self.root_container, keys, events, element_height)
        self.window_manager = WindowManager()
    
    def run(self):
        Draw.Register(self._gui, self.event_manager.key_event, self.event_manager.element_event)
