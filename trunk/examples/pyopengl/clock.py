# -*- coding: utf-8 -*-
import os, sys
from time import localtime, time

# FIXME: evilness!
try:
    import bui
except ImportError:
    bui_path = os.path.normpath(sys.path[0])
    bui_path = bui_path[:bui_path.rfind('/')]
    bui_path = bui_path[:bui_path.rfind('/')]
    sys.path.append(bui_path)

from bui.frontend.pyopengl.window import WindowManager
from bui.utils.color import generate_color
from bui.utils.math import lerp
from bui.utils.meta import AllMethodsStatic

# TODO: make it possible to use an element as root (scales to window width/height unless set otherwise!)
# TODO: check how to handle label text width (scales as the label width scales???)

# note that this sets up a single window with given attributes
configuration = '''
    label: Clock test
    width: 400
    height: 200
    start_timers: True
    hotkeys: hotkeys
    structure: root_structure
    element_height: 20
'''

# should use this instead!
class UIStructureProperOne():
    root_structure = '''
        Label:
            name: current_time
    '''

# even neater one!
class UIStructureProperOneSecond():
    root_structure = '''
        Label: current_time
    '''

# TODO: check how element_height should scale
class UIStructure():
    root_structure = '''
    HorizontalLayout:
        bg_color: [1.0, 0.0, 0.0]
        height: 80 # children should scale to fit height! if not set, use 'auto' height
        children:
            - Label:
                name: current_time
                #height: 80 # <= parent height if set
    '''

class Hotkeys():
    hotkeys = '''
        q: quit_script
    '''

class Events(AllMethodsStatic):
    def quit_script(elem, timers):
        sys.exit()

class Timers(AllMethodsStatic):
    def update_clock(root_elem, timer, timers):
        ''' interval=0.5 '''
        current_time = get_current_time_as_formatted_string()
        clock = root_elem.find_child(name='current_time')
        clock.label = current_time
    
    def update_clock_color(root_elem, timer, timers):
        ''' interval=1/24 '''
        clock = root_elem.find_child(name='current_time')
        current_time = time()
        
        fac = (current_time-clock.new_color_start_time) / clock.new_color_interval
        fac = min(fac, 1.0)
        
        clock.bg_color = lerp(clock.new_color, clock.old_color, fac)
    
    def generate_new_clock_color(root_elem, timer, timers):
        ''' interval=5 '''
        clock = root_elem.find_child(name='current_time')
        
        if not hasattr(clock, 'new_color'):
            clock.new_color = generate_color()
        
        clock.old_color = clock.new_color
        clock.new_color = generate_color()
        
        clock.new_color_start_time = time()
        clock.new_color_interval = timer.interval_in_seconds

def get_current_time_as_formatted_string(separator=':'):
    ''' @return: current time formatted as hh:mm:ss by default '''
    time_list = localtime()[3:6]
    time_list_items_as_string = ['%02d%s' % (i, separator) for i in time_list]
    return ''.join(time_list_items_as_string)[:-1]

if __name__ == '__main__':
    window_manager = WindowManager(configuration, UIStructure, Hotkeys, Events, Timers)
    window_manager.run()
