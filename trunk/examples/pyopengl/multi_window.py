# -*- coding: utf-8 -*-

from bui.frontend.pyopengl.window import WindowManager
from bui.utils.meta import AllMethodsStatic

# TODO: how to handle subwindows???

# TODO: should pass reference to timers as well (alter other timers using timer!) add this to regular events and constraints too!

conf = '''
    Window:
        name: root_window
        label: Some window
        width: 600
        bg_color: blue # extend this??? bg as texture/gradient/color/etc. ? implement color names too
        subwindows:
            - Window: # this subwindow should take slice of 200 px from left side of root? (does root alter coords or width due to this?)
                name: subwindow
                alignment: left
                width: 200
'''

# TODO: make it possible to define config file for window
# perhaps something along this might work:
window_configuration = '''
    label: Clock test
    width: 400
    height: 200
    # show_fps: True # False by default
    # logging: True # False by default
    # full_screen: True # False by default if not set
    # v_sync: True # needed even?
    # alignment: left # could be center by default if not set
    # default_node_height: 50
    start_timers: True # False by default if not set
    # layout: some_layout # uses root_layout by default if not set
    # hotkeys: some_keys # checks the hotkey container for this name. uses the first found by default?
    # initializer: some_initializer # uses the first found by default if not set?
'''

# should hot keys be global?
# how to handle active context? (window context can be set active if mouse if over window. or it can be global (hotkeys affect each window!))
# should it be possible to set context even on lower level? (ie. mouse over layout)

global_configuration = '''
    hotkeys: some_global_hotkeys # these hotkeys can be used globally (not context dependant!)
'''


# how to handle multiple windows???
# test this in separate example
# note that full screen is a special case!
window_configuration = '''
    - Window:
        name: Some window
        width: 300
        height: 300
        alignment: left
        layout: some_structure # use root_structure if not defined?
        initializer: initializer_func # if no initializer is defined, don't use one
        hotkeys: some_keys
        constraints: some_constraints
    - Window:
        name: Another window
        width: 200
        height: 100
        alignment: right
        layout: other_structure
        hotkeys: other_keys
        timers: some_timers
'''

# class Configuration(): ???

# combine all conf to one? global settings affect each window!
configuration = '''
    - Global:
        hotkeys: some_hotkeys
        constraints: global_constraints
        window_width: 300 # use this if width is not set for window
        window_height: 500 " use this if height is not set for window
        # other global defaults?
        default_node_height: 40 # applies globally unless set per window
        timers: global_timers # these are seen by all windows
    - Windows:
        - Window:
            name: some_window
            width: 400
            height: 200
            alignment: left
            visible: False # make window invisible, True by default
            timers: some_timers # own timers. sees these in addition to global ones
        - Window:
            name: other window
            constraints: local_constraints # uses these in addition of global ones
'''

class Initializers(AllMethodsStatic):
    def ui_initialize(root_elem, event_manager): # should use timer_manager instead
        pass
        # timer_manager.timers.start() # starts all timers
        # timer_manager.timers.stop() # stops all timers
        # note that it's possible to start/top/pause individual timers as well!
        #event_manager.create_timer(update_clock, interval=0.5) # update twice per second
        #event_manager.create_timer(generate_new_clock_color, interval=5.0)
        #event_manager.create_timer(update_clock_color, interval=1/24.0)
        # note that this starts timer!

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events, ui_initializer=ui_initialize)
    app.run()
