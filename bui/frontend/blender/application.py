# -*- coding: utf-8 -*-
from Blender import BGL, Draw, Window
from Blender.Window import Types

from bui.backend.application import BaseApplication

# add elements to backend serializer so it can find them
import bui.backend.serializer
import element

for var_name, var_item in vars(element).items():
    if type(var_item) == type:
        setattr(bui.backend.serializer, var_name, var_item)

from event import EventManager
from layout import LayoutManager
from window import WindowManager

from keys import BLENDER_KEYS

global app # FIXME: get rid of this

class Event():
    pass

def check_state_events(elem):
    global app
    
    mouse_coords = app.window_manager.get_mouse_coordinates()
    triggered_event = app.event_manager.check_state_events(mouse_coords)
    
    if triggered_event:
        Window.Redraw(Types.SCRIPT)

class Application(BaseApplication):
    def __init__(self, structure, keys, events=None, constraints=None,
                 ui_initializer=None, element_height=20):
        super(Application, self).__init__(structure, keys, events,
                                          constraints, ui_initializer, element_height)
        
        self.event_manager = EventManager(self.root_container, keys, events)
        
        for event in ('mouse_x', 'mouse_y'):
            self.event_manager.key_events[BLENDER_KEYS[event]] = Event()
            self.event_manager.key_events[BLENDER_KEYS[event]].press = check_state_events   
        
        self.window_manager = WindowManager()
        self.layout_manager = LayoutManager(self.window_manager, self.root_container)
        
        global app
        app = self
    
    def run(self):
        super(Application, self).run()
        Draw.Register(self.redraw, self.event_manager.key_event, self.event_manager.element_event)
