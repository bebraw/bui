# -*- coding: utf-8 -*-
import os, sys

# FIXME: evilness!
bui_path = os.path.normpath(sys.path[0])
bui_path = bui_path[:bui_path.rfind('/')]
bui_path = bui_path[:bui_path.rfind('/')]
sys.path.append(bui_path)

from bui.frontend.pyopengl.window import WindowManager
from bui.utils.meta import AllMethodsStatic

# TODO: should bg color of layout cascade to its children like default values do?

configuration = '''
    label: Free layout test
    width: 640
    height: 480
    hotkeys: hotkeys
    structure: root_structure
    default_node_height: 20
    bg_color: [0.8, 0.8, 0.8]
'''

class UIStructure():
    root_structure = '''
    FreeLayout:
        name: free root
        bg_color: [0.2, 0.5, 0.6]
        children:
            - VerticalLayout:
                x: 10
                y: 20
                bg_color: [0.0, 0.1, 0.4]
                min_width: 300
                max_width: 600
                height: 100
                children:
                    - Label:
                        label: Some label
                        color: [1.0, 0.0, 0.0]
                    - Label:
                        label: Another label
                        color: [1.0, 0.0, 0.0]
                        alpha: 0.5
                    - Separator:
                        label: Test separator
                    - Label:
                        label: Hello world!
                        color: [0.1, 0.4, 0.1] # TODO: probably color: green would be nicer
                    - Label:
                        label: Hello world 2!
                        color: [1.0, 1.0, 0.0]
            - HorizontalLayout:
                x: 50
                y: 150
                height: 100
                bg_color: [0.0, 0.0, 1.0]
                default_node_height: 20
                default_node_width: 100
                children:
                    - Label:
                        label: First child
                        bg_color: [0.2, 0.5, 0.6]
                        color: [1.0, 1.0, 0.0]
                        height: 30
                    - Label:
                        label: Second child
                        bg_color: [1.0, 0.0, 0.0]
                        color: [1.0, 1.0, 0.0]
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
