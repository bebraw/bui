import fnmatch

import bpy
from Blender import Draw

from bui.container import Fill

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
                        name: Image Filter v0.1
                    - PushButton:
                        name: X
                        tooltip: Quit script
                        event_handler: quit_script
                        width: 20
            - HorizontalContainer:
                children:
                    - TextBox:
                        name: Filter
                        tooltip: Please enter image filter here
                        max_input_length: 40
                    - Fill:
                        width: 400
            - Fill:
                height: 10
            - HorizontalContainer:
                name: results
    '''

hotkeys = '''
q: quit_script
'''

class Events():
    @staticmethod
    def quit_script(elem):
        Draw.Exit()
    
    @staticmethod
    def filter(elem):
        filter_clause = elem.value
        root_elem = elem.find_root_element()
        results_elem = root_elem.find_child(name='results')
        results_elem.remove_children()
        
        for image in bpy.data.images:
            if fnmatch.filter([image.name, ], filter_clause):
                new_image = Image(file=image.name, width=200)
                results_elem.add_child_structure(new_image)
                results_elem.add_child_structure(Fill(width=10))

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events)
    app.run()