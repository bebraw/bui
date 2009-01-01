# -*- coding: utf-8 -*-
from Blender import Draw

from bui.frontend.blender.application import Application

from bui.utils.meta import AllMethodsStatic

class UIStructure():
    root_structure = '''
    VerticalLayout:
        name: root_vertical
        width: 400
        children:
            - HorizontalLayout:
                name: test_hori
                children:
                    - Icon:
                        name: blender
                    - Icon:
                        name: sequence
                        height: 40
                    - Icon:
                        name: action
                        width: 30
                    - Icon:
                        name: node
                        height: 40
                        width: 40
                    - Label:
                        name: Test script
                    - PushButton:
                        name: X
                        tooltip: Quit script
                        event_handler: quit_script
                        width: 20
            - Fill:
                height: 10
            - HorizontalLayout:
                name: last_hori
                children:
                    - PushButton:
                        name: Do something
                        tooltip: Add some tool here
                        width: 100
                    - Slider:
                        name: Test slider
            - HorizontalLayout:
                children:
                    - Number:
                        name: Some number
                        value: 0.5
                    - Number:
                        name: Another number
                    - IntNumber:
                        name: Some int number
                        max: 100
            - Fill:
                height: 30
            - HorizontalLayout:
                children:
                    - Fill:
                        width: 20
                    - Image:
                        file: Mandril.png
                    - Label:
                        name: Foobar
                    - Image:
                       file: Mandril.png
                       height: 100
            - HorizontalLayout:
                children:
                    - Label:
                       name: 'SVG image:'
                    - Image:
                       file: home.svg
                       height: 100
                       width: 200
            - Fill:
                height: 15
            - HorizontalLayout:
                children:
                    - Label:
                        name: Foofoo
                    - Number:
                        name: Some number
                    - Fill:
                        width: 50
                    #- Normal:
                    #    width: 50
                    - ColorPicker:
                        width: 50
            - Fill:
                height: 15
            - HorizontalLayout:
                children:
                    - Image:
                       file: Mandril.png
                       width: 500
    '''

hotkeys = '''
d:
    press: d_was_pressed
    release: d_was_released
s: foobar
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
        Draw.Exit()

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events)
    app.run()
