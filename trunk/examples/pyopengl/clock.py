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

# note that this sets up a single window with given attributes
configuration = '''
    label: Clock test
    width: 1000
    height: 200
    start_timers: True
    hotkeys: hotkeys
    structure: root_structure
    #default_node_height: 20
'''

# TODO: auto doesn't work with HorizontalLayout as it should?
# TODO: see if width should affect label text too (should text fit to given width?)
class UIStructure():
    root_structure = '''
    VerticalLayout:
        children:
            - Label:
                name: current_time
    '''

class Hotkeys():
    hotkeys = '''
        q: quit_script
    '''

class Events(AllMethodsStatic):
    def quit_script(elem, timers):
        sys.exit()

class Timers(AllMethodsStatic):
    def update_clock(root_layout, timer, timers):
        ''' interval=0.5 '''
        current_time = get_current_time_as_formatted_string()
        clock = root_layout.find_child(name='current_time')
        clock.label = current_time
    
    def update_clock_color(root_layout, timer, timers):
        ''' interval=1/24 '''
        clock = root_layout.find_child(name='current_time')
        current_time = time()
        
        fac = (current_time-clock.new_color_start_time) / clock.new_color_interval
        fac = min(fac, 1.0)
        
        clock.bg_color = lerp(clock.new_color, clock.old_color, fac)
    
    def generate_new_clock_color(root_layout, timer, timers):
        ''' interval=5 '''
        clock = root_layout.find_child(name='current_time')
        
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
