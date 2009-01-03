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
                        label: Test script
                    - PushButton:
                        name: quit_script
                        label: X
                        tooltip: Quit script
                        width: 20
            - Fill:
                height: 10
            - HorizontalLayout:
                name: last_hori
                children:
                    - PushButton:
                        label: Do something
                        tooltip: Add some tool here
                        width: 100
                    - Slider:
                        label: Test slider
            - HorizontalLayout:
                children:
                    - Number:
                        label: Some number
                        value: 0.5
                    - Number:
                        label: Another number
                    - IntNumber:
                        label: Some int number
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
                        label: Foobar
                    - Image:
                       file: Mandril.png
                       height: 100
            - HorizontalLayout:
                children:
                    - Label:
                       label: 'SVG image:'
                    - Image:
                       file: home.svg
                       height: 100
                       width: 200
            - Fill:
                height: 15
            - HorizontalLayout:
                children:
                    - Label:
                        label: Foofoo
                    - Number:
                        label: Some number
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
