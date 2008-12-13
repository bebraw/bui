import fnmatch

import bpy
from Blender import Draw

from bui.container import Fill, VerticalContainer
from bui.utils import AllMethodsStatic

from bui.blender.application import Application
from bui.blender.element import Image, Label

class UIStructure():
    root_structure = '''
    VerticalContainer:
        bg_color: [0.95, 0.95, 0.8]
        width: 600
        children:
            - HorizontalContainer:
                bg_color: [1.0, 0.0, 0.0]
                children:
                    - Label:
                        bg_color: [0.5, 0.5, 0.5]
                        name: Image Filter v0.2
                    - PushButton:
                        name: X
                        tooltip: Quit script
                        event_handler: quit_script
                        width: 20
            - HorizontalContainer:
                children:
                    - TextBox:
                        bg_color: [0.0, 1.0, 0.0]
                        name: Filter
                        tooltip: Please enter image filter here
                        max_input_length: 40
                        width: 200
            - Fill:
                height: 10
            - HorizontalContainer:
                name: results
    '''

hotkeys = '''
q: quit_script
'''

class Events(AllMethodsStatic):
    def quit_script(elem):
        Draw.Exit()
    
    def filter(elem):
        filter_clause = elem.value
        root_elem = elem.find_root_element()
        results_elem = root_elem.find_child(name='results')
        results_elem.remove_children()
        
        for image in bpy.data.images:
            if fnmatch.filter([image.name, ], filter_clause):
                v_container = VerticalContainer(bg_color=[0.7, 0.7, 0.7])
                
                new_image = Image(file=image.name, width=200)
                v_container.add_child_structure(new_image)
                v_container.add_child_structure(Label(name=image.name))
                
                results_elem.add_child_structure(v_container)
                results_elem.add_child_structure(Fill(width=10))

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events)
    app.run()