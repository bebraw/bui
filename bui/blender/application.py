# -*- coding: utf-8 -*-
from Blender import BGL, Draw, Window
from Blender.Window import Types

from bui.application import BaseApplication

# add elements to backend serializer so it can find them (probably not the cleanest solution)
import bui.serializer
import bui.blender.element

for module_item_name in dir(bui.blender.element):
    module_item = getattr(bui.blender.element, module_item_name)
    
    if type(module_item) == type:
        setattr(bui.serializer, module_item_name, module_item)

from bui.blender.event import EventManager
from bui.blender.layout import LayoutManager
from bui.blender.window import WindowManager

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
        
        self.event_manager.key_events[BLENDER_KEYS['mouse_x']] = Event()
        self.event_manager.key_events[BLENDER_KEYS['mouse_x']].press = check_state_events
        
        self.event_manager.key_events[BLENDER_KEYS['mouse_y']] = Event()
        self.event_manager.key_events[BLENDER_KEYS['mouse_y']].press = check_state_events
        
        self.window_manager = WindowManager()
        self.layout_manager = LayoutManager(self.window_manager, self.root_container, element_height)
        
        global app
        app = self
    
    def run(self):
        super(Application, self).run()
        Draw.Register(self.gui, self.event_manager.key_event, self.event_manager.element_event)
    
    def gui(self):
        super(Application, self).gui()
