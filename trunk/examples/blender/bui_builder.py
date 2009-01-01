# -*- coding: utf-8 -*-
from Blender import Draw

import bui.backend.layout
from bui.utils.meta import AllMethodsStatic

import bui.frontend.blender.element # FIXME: element has been split to modules!
from bui.frontend.blender.application import Application
from bui.frontend.blender.element import Label

class UIStructure():
    root_structure = '''
    VerticalLayout:
        width: 600
        children:
            - HorizontalLayout:
                bg_color: [0.9, 0.9, 0.9]
                children:
                    - Label:
                        name: BUI Builder v0.1
                    - PushButton:
                        name: X
                        tooltip: Quit script
                        event_handler: quit_script
                        width: 20
            - HorizontalLayout:
                children:
                    - VerticalLayout:
                        width: 150
                        children:
                            - Label:
                                name: "UI Objects:"
                            - VerticalLayout:
                                children:
                                    - Label:
                                        name: "Layouts:"
                                    - VerticalLayout:
                                        name: layouts
                            - VerticalLayout:
                                children:
                                    - Label:
                                        name: "Elements:"
                                    - VerticalLayout:
                                        name: elements
                    - VerticalLayout:
                        children:
                            - Label:
                                name: "Build UI here."
                    - VerticalLayout:
                        width: 150
                        children:
                            - Label:
                                name: "Properties:"
    '''

hotkeys = '''
q: quit_script
'''

class Events(AllMethodsStatic):
    def quit_script(elem):
        Draw.Exit()

def populate_container(root_elem, container_name, module):
    containers_elem = root_elem.find_child(name=container_name)
    
    for module_item_name in dir(module):
        module_item = getattr(module, module_item_name)
        
        if type(module_item) == type:
            containers_elem.append(Label(name=module_item_name))

def ui_initialize(root_elem):
    populate_container(root_elem, 'layouts', bui.backend.layout)
    populate_container(root_elem, 'elements', bui.blender.element)

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events, ui_initializer=ui_initialize)
    app.run()
