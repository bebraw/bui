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
from bui.utils.meta import AllMethodsStatic

configuration = '''
    label: Node editor
    width: 800
    height: 600
    hotkeys: hotkeys
    structure: root_structure
    #default_node_height: 20
'''

class UIStructure():
    root_structure = '''
    HorizontalLayout:
        bg_color: [0.2, 0.5, 0.5]
        children:
            - VerticalLayout:
                #height_mode: auto
                height: 600 # TODO: should be auto by default!
                width: 200
                bg_color: [0.4, 0.0, 0.0]
            - FreeLayout:
                height: 600 # TODO: see above
                bg_color: [0.0, 0.4, 0.0]
            - VerticalLayout:
                height: 600 # TODO: see above
                width: 200
                bg_color: [0.0, 0.0, 0.4]
                children:
                    #- FreeLayout:
                    #    children:
                    #        - Label:
                    #            label: Viewport goes here
                    #            bg_color: [0.3, 0.3, 0.0]
                    #            height: 20
                    - VerticalLayout: # XXX: if FreeLayout is provided before, renders below parent!
                        #height: 300
                        #width: 150
                        bg_color: [0.7, 0.0, 0.3]
                        children:
                            - Label:
                                label: Attributes go here # renders to wrong location!
                                bg_color: [0.0, 0.0, 0.3]
                                height: 20
    '''

class Hotkeys():
    hotkeys = '''
        q: quit_script
    '''

class Events(AllMethodsStatic):
    def quit_script(elem):
        sys.exit()

def get_current_time_as_formatted_string(separator=':'):
    ''' @return: current time formatted as hh:mm:ss by default '''
    time_list = localtime()[3:6]
    time_list_items_as_string = ['%02d%s' % (i, separator) for i in time_list]
    return ''.join(time_list_items_as_string)[:-1]

if __name__ == '__main__':
    window_manager = WindowManager(configuration, UIStructure, Hotkeys, Events)
    window_manager.run()
