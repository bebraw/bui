# -*- coding: utf-8 -*-
import pyglet
import sys
import os.path

# TODO: separate test/example part to other files

# TODO: rename Application to BaseApplication so each specialization can be named as Application
# Do the same also for other main classes

# FIXME: evilness!
bui_path = os.path.normpath(sys.path[0])
bui_path = bui_path[:bui_path.rfind('/')]
bui_path = bui_path[:bui_path.rfind('/')]
sys.path.append(bui_path)

from bui.application import BaseApplication
from bui.event import BaseEventManager

class EventManager(BaseEventManager):
    def __init__(self, root_container, keys, events, element_height):
        super(EventManager, self).__init__(root_container, keys, events, element_height)
    
    # TODO: needs pyglet key mapping and rerouting!

class PygletWindow(pyglet.window.Window):
    def __init__(self):
        super(PygletWindow, self).__init__()
        
        self.label = pyglet.text.Label('Hello, world!')
    
    def on_draw(self):
        self.clear()
        self.label.draw()
    
    # this should go to eventmanager (check @window.event !!!)
    def on_key_press(self, symbol, modifiers):
        print symbol, modifiers
    
    # this should go to eventmanager
    def on_key_release(self, symbol, modifiers):
        print symbol, modifiers

class Application(BaseApplication): #pyglet.window.Window):
    def __init__(self, structure, keys, events=None, constraints=None, element_height=20):
        super(Application, self).__init__(structure, keys, events, constraints, element_height)
        
        #self.app = BaseApplication(structure, keys, events, constraints, element_height)
        #super(PygletApplication, self).__init__(structure, keys, events, constraints, element_height)
        
        self.pyglet_window = PygletWindow() # the idea is that PygletApplication contains pyglet Window
        # then the events are rerouted so that calls actually go via event_manager! (figure out neat
        # way to do this)
        
        self.event_manager = EventManager(self.root_container, keys, events, element_height)
        #self.window_manager = PygletWindowManager()
    
    def run(self):
        pyglet.app.run()

class UIStructure():
    root_structure = '''
    VerticalContainer:
        name: root_vertical
        width: 400
    '''

hotkeys = '''
d:
    press: d_was_pressed
    release: d_was_released
s: foobar
q: quit_script
'''

class Events():
    @staticmethod
    def d_was_pressed(elem):
        print 'you pressed d!'
    
    @staticmethod
    def d_was_released(elem):
        print 'you released d!'
    
    @staticmethod
    def foobar(elem):
        print 'foobar'
    
    @staticmethod
    def quit_script(elem):
        Draw.Exit()

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events)
    app.run()
