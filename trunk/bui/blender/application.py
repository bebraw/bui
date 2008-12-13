# -*- coding: utf-8 -*-
from Blender import BGL, Draw, Window
from Blender.Window import Types

from bui.application import BaseApplication
from bui.abstract import AbstractObject

from bui.blender.event import EventManager
from bui.blender.layout import LayoutManager
from bui.blender.window import WindowManager

from keys import BLENDER_KEYS

global app # FIXME: get rid of this

# override render_bg_color (in right place?)
def render_bg_color(self):
    if self.bg_color:
        BGL.glColor3f(*self.bg_color)
        BGL.glRectf(self.x, self.y, self.x + self.width, self.y + self.height)

setattr(AbstractObject, 'render_bg_color', render_bg_color)

class Event():
    pass

def check_state_events(elem):
    global app
    
    mouse_coords = app.window_manager.get_mouse_coordinates()
    triggered_event = app.event_manager.check_state_events(mouse_coords)
    
    if triggered_event:
        Window.Redraw(Types.SCRIPT)

class Application(BaseApplication):
    def __init__(self, structure, keys, events=None, constraints=None, element_height=20):
        super(Application, self).__init__(structure, keys, events, constraints, element_height)
        
        self.event_manager = EventManager(self.root_container, keys, events)
        
        self.event_manager.key_events[BLENDER_KEYS['mouse_x']] = Event()
        self.event_manager.key_events[BLENDER_KEYS['mouse_x']].press = check_state_events
        
        self.event_manager.key_events[BLENDER_KEYS['mouse_y']] = Event()
        self.event_manager.key_events[BLENDER_KEYS['mouse_y']].press = check_state_events
        
        self.layout_manager = LayoutManager(self.root_container, element_height)
        self.window_manager = WindowManager()
        
        global app
        app = self
    
    def run(self):
        super(Application, self).run()
        Draw.Register(self.gui, self.event_manager.key_event, self.event_manager.element_event)
    
    def gui(self):
        super(Application, self).gui()
