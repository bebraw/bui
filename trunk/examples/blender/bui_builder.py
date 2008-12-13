# -*- coding: utf-8 -*-
from Blender import Draw

import bui.container
from bui.utils import AllMethodsStatic

import bui.blender.element
from bui.blender.application import Application
from bui.blender.element import Label

class UIStructure():
    root_structure = '''
    VerticalContainer:
        width: 600
        children:
            - HorizontalContainer:
                bg_color: [0.9, 0.9, 0.9]
                children:
                    - Label:
                        name: BUI Builder v0.1
                    - PushButton:
                        name: X
                        tooltip: Quit script
                        event_handler: quit_script
                        width: 20
            - HorizontalContainer:
                children:
                    - VerticalContainer:
                        width: 150
                        children:
                            - Label:
                                name: "UI Objects:"
                            - VerticalContainer:
                                children:
                                    - Label:
                                        name: "Containers:"
                                    - VerticalContainer:
                                        name: containers
                            - VerticalContainer:
                                children:
                                    - Label:
                                        name: "Elements:"
                                    - VerticalContainer:
                                        name: elements
                    - VerticalContainer:
                        children:
                            - Label:
                                name: "Build UI here."
                    - VerticalContainer:
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
            module_name = module_item.__name__
            print module_name
            containers_elem.append(Label(name=module_name))

def ui_initialize(root_elem):
    populate_container(root_elem, 'containers', bui.container)
    populate_container(root_elem, 'elements', bui.blender.element)

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events, ui_initializer=ui_initialize)
    app.run()
