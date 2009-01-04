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

# note that this sets up a single window with given attributes
configuration = '''
    label: Clock test
    width: 400 # if not set, give exception (add full screen option!) (special case: there is global window width setting (use this instead!). see multi_window.py)
    height: 200 # if not set, give exception
    start_timers: True # False by default if not set
    hotkeys: hotkeys # checks the hotkey container for this name. uses the first found by default?
    structure: root_structure # should check for root_structure automagically???
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
        children:
            - Label:
                name: current_time
                bg_color: [0.0, 1.0, 0.0]
                #height: 80
                #width: 100 # TODO: should this case scale text to fit???
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
        ''' interval=5.0 '''
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
