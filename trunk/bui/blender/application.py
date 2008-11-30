# -*- coding: utf-8 -*-
from Blender import Draw, Window
from Blender.Window import Types

from bui.application import BaseApplication
from bui.coordinate import coordinate_from_tuple

from bui.blender.event import EventManager
from bui.blender.window import WindowManager

from keys import BLENDER_KEYS

USE_STATE_EVENTS = False

class Event():
    pass

def check_state_events(elem):
    Window.Redraw(Types.SCRIPT)

class Application(BaseApplication):
    def __init__(self, structure, keys, events=None, constraints=None, element_height=20):
        super(Application, self).__init__(structure, keys, events, constraints, element_height)
        
        self.event_manager = EventManager(self.root_container, keys, events, element_height)
        
        if USE_STATE_EVENTS:
            self.event_manager.key_events[BLENDER_KEYS['mouse_x']] = Event()
            self.event_manager.key_events[BLENDER_KEYS['mouse_x']].press = check_state_events
            
            self.event_manager.key_events[BLENDER_KEYS['mouse_y']] = Event()
            self.event_manager.key_events[BLENDER_KEYS['mouse_y']].press = check_state_events
        
        self.window_manager = WindowManager()
    
    def run(self):
        Draw.Register(self.gui, self.event_manager.key_event, self.event_manager.element_event)
    
    def gui(self):
        mouse_coords = coordinate_from_tuple(Window.GetMouseCoords())
        self.event_manager.check_state_events(mouse_coords)
        
        super(Application, self).gui()
