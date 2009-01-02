# -*- coding: utf-8 -*-
import fnmatch

import bpy
from Blender import Draw

from bui.backend.element.fill import Fill
from bui.backend.layout import VerticalLayout

from bui.frontend.blender.application import Application
from bui.frontend.blender.element.image import Image
from bui.frontend.blender.element.label import Label

from bui.utils.meta import AllMethodsStatic

class UIStructure():
    root_structure = '''
    VerticalLayout:
        bg_color: [0.95, 0.95, 0.8]
        width: 600
        children:
            - HorizontalLayout:
                bg_color: [1.0, 0.0, 0.0]
                children:
                    - Label:
                        label: Image Filter v0.2
                        bg_color: [0.5, 0.5, 0.5]
                    - PushButton:
                        label: X
                        tooltip: Quit script
                        event_handler: quit_script
                        width: 20
            - HorizontalLayout:
                children:
                    - TextBox:
                        label: Filter
                        bg_color: [0.0, 1.0, 0.0]
                        tooltip: Please enter image filter here
                        max_input_length: 40
                        width: 200
            - Separator:
                label: Results
                height: 20
            - HorizontalLayout:
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
                v_layout = VerticalLayout(bg_color=[0.7, 0.7, 0.7])
                
                new_image = Image(file=image.name, width=200)
                v_layout.append(new_image)
                v_layout.append(Label(label=image.name))
                
                results_elem.append(v_layout)
                results_elem.append(Fill(width=10))

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events)
    app.run()
