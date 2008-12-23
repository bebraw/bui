# -*- coding: utf-8 -*-
from Blender import Draw

from bui.utils import AllMethodsStatic

from bui.blender.application import Application
from bui.blender.element import Image

class UIStructure():
    root_structure = '''
    VerticalContainer:
        width: 600
        children:
            - HorizontalContainer:
                children:
                    - Label:
                        name: Amazing state event test v0.1
            - Fill:
                height: 10
            - HorizontalContainer:
                children:
                    - Image:
                        file: Mandril.png
                        height: 100
                        events:
                            on_mouse_over: show_big_image
            - HorizontalContainer:
                name: big_image
    '''

hotkeys = '''
q: quit_script
'''

class Events(AllMethodsStatic):
    def quit_script(elem):
        Draw.Exit()
    
    def show_big_image(root_elem):
        big_image_elem = root_elem.find_child(name='big_image')
        big_image_elem.append(Image(file='Mandril.png', width=10))

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events)
    app.run()
