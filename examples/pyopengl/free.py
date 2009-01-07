# -*- coding: utf-8 -*-
import os, sys

# FIXME: evilness!
bui_path = os.path.normpath(sys.path[0])
bui_path = bui_path[:bui_path.rfind('/')]
bui_path = bui_path[:bui_path.rfind('/')]
sys.path.append(bui_path)

from bui.frontend.pyopengl.window import WindowManager
from bui.utils.meta import AllMethodsStatic

configuration = '''
    label: Free layout test
    width: 640
    height: 480
    hotkeys: hotkeys
    structure: root_structure
    default_node_height: 20
'''

class UIStructure():
    root_structure = '''
    FreeLayout:
        name: free root
        bg_color: [0.2, 0.5, 0.6]
        width: auto
        height: 300 # add auto setting? without width/height should use window dimensions? (x/y?)
        children:
            - VerticalLayout:
                x: 10
                y: 20
                min_width: 300
                max_width: 600
                height: 100
                children:
                    - Label:
                        label: Some label
                    - Label:
                        label: Another label
                        alpha: 0.5
                    - Separator:
                        label: Test separator
                    - Label:
                        label: Hello world!
                        color: [0.0, 1.0, 0.0] # TODO: probably color: green would be nicer
                    - Label:
                        label: Hello world 2!
                        color: [1.0, 1.0, 0.0]
            - HorizontalLayout:
                x: 50
                y: 150
                width: auto
                height: 100
                bg_color: [0.5, 0.2, 0.2]
                children:
                    - Label:
                        label: First child
                        width: 300
                    - Label:
                        label: Second child
                        bg_color: [0.3, 0.8, 0.5]
                        width: 200
    '''

class Hotkeys():
    hotkeys = '''
    q: quit_script
    '''

class Events(AllMethodsStatic):
    def quit_script(elem):
        sys.exit()

if __name__ == '__main__':
    window_manager = WindowManager(configuration, UIStructure, Hotkeys, Events)
    window_manager.run()
