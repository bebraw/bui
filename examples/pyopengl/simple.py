# -*- coding: utf-8 -*-
import os, sys

# FIXME: evilness!
bui_path = os.path.normpath(sys.path[0])
bui_path = bui_path[:bui_path.rfind('/')]
bui_path = bui_path[:bui_path.rfind('/')]
sys.path.append(bui_path)

from bui.frontend.pyopengl.application import Application

from bui.utils.meta import AllMethodsStatic

class UIStructure():
    root_structure = '''
    VerticalContainer:
        name: root_vertical
        bg_color: [0.2, 0.5, 0.6]
        width: auto
        children:
            - VerticalContainer:
                children:
                    - Label:
                        name: Some label
                    - Label:
                        name: Another label
                        alpha: 0.5 # test alpha
                    - Separator:
                        name: Test separator
                    - Label:
                        name: Hello world!
                        color: [0.0, 1.0, 0.0] # probably color: green would be nicer
            - HorizontalContainer:
                bg_color: [0.5, 0.2, 0.2]
                children:
                    - Label:
                        name: First child
                        width: 100
                    - Label:
                        name: Second child
                        bg_color: [0.3, 0.8, 0.5]
                        width: 200
    '''

hotkeys = '''
q: quit_script
'''

class Events(AllMethodsStatic):
    def d_was_pressed(elem):
        print 'you pressed d!'
    
    def d_was_released(elem):
        print 'you released d!'
    
    def foobar(elem):
        print 'foobar'
    
    def quit_script(elem):
        sys.exit()

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events, window_name='test window')
    app.run()
