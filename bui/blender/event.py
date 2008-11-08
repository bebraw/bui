# -*- coding: utf-8 -*-
from Blender import Window
from Blender.Window import Types

from bui.event import EventManager

'''
TODO:
-self.events[Draw.ESCKEY] should be handled elsewhere! (in event list!)
'''

class BlenderEventManager(EventManager):
    def __init__(self, root_container, element_height):
        super(BlenderEventManager, self).__init__(root_container, element_height)
        
        self.events[Draw.ESCKEY] = quit_script # TODO: get rid of this line
    
    def button_event(self, evt):
        super(BlenderEventManager, self).__init__(evt)
        
        Window.Redraw(Types.VIEW3D) # TODO: too specific?
        Window.Redraw(Types.SCRIPT)
