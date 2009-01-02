# -*- coding: utf-8 -*-
import os, sys
from time import localtime

# FIXME: evilness!
bui_path = os.path.normpath(sys.path[0])
bui_path = bui_path[:bui_path.rfind('/')]
bui_path = bui_path[:bui_path.rfind('/')]
sys.path.append(bui_path)

from bui.frontend.pyopengl.application import Application
from bui.utils.meta import AllMethodsStatic

# TODO: make it possible to define config file for window
# TODO: make it possible to use an element as root (scales to window width/height unless set otherwise!)

class UIStructure():
    root_structure = '''
    HorizontalLayout:
        bg_color: [1.0, 0.0, 0.0]
        # width: 200 # doesn't work as it should?
        children:
            - Label:
                name: current_time
                bg_color: [0.0, 1.0, 0.0]
                height: 80
    '''

hotkeys = '''
q: quit_script
'''

class Events(AllMethodsStatic):
    def quit_script(elem):
        sys.exit()

# should put to Events?
# could use something like following then
#@timer(name='clock_timer', interval=0.5) # this should trigger timer automatically?
def update_clock(root_elem):
    current_time = get_current_time_as_formatted_string()
    clock = root_elem.find_child(name='current_time')
    clock.label = current_time

def get_current_time_as_formatted_string(separator=':'):
    ''' returns current time formatted as hh:mm:ss by default '''
    time_list = localtime()[3:6]
    time_list_items_as_string = ['%02d%s' % (i, separator) for i in time_list]
    return ''.join(time_list_items_as_string)[:-1]

def ui_initialize(root_elem, event_manager):
    # just temp hack to get timer running. could try decorator scheme instead
    event_manager.create_timer(update_clock, interval=0.5) # update twice per second
    # note that this starts timer!
    # FIXME: timer slows down app when resizing!

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events, ui_initializer=ui_initialize)
    app.run()
