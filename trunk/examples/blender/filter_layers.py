# -*- coding: utf-8 -*-
from Blender import Draw, Scene, Window

from bui.backend.serializer import unserialize

from bui.frontend.blender.application import Application

from bui.utils.meta import AllMethodsStatic

from object_filter import ObjectFilter

'''
TODO:
-improve data filter (give another menu with data types if data is selected. remember OR toggle too!)
-add control logic and hook up filters with the system
-drag and drop (ie. move layers/filters around)
-filter by group/name + possibility to filter multiple data types at once (mesh, lamp, etc. -> convert to list that is passed onto func)
-improve mapping between filtering type option menu and filter backend!
-make it possible to restore old layers/filters (Registry module? implement serialize and @persistent)
'''

def clamp(val, min_val, max_val):
    return min(max(val, min_val), max_val)

def assign_all_objects_to_layer(layer):
    scn = Scene.GetCurrent()
    
    for ob in scn.objects:
        ob.layers = [layer, ]

class UIStructure():
    root_structure = '''
    VerticalLayout:
        width: 400
        children:
            - HorizontalLayout:
                children:
                    - Label:
                        label: Filter layers v0.9
                    - PushButton:
                        name: quit_script
                        label: X
                        tooltip: Quit script
                        width: 20
            - Fill:
                height: 10
            - VerticalLayout:
                name: layers
                children:
                    - UIStructure:
                        name: layer_structure
            - HorizontalLayout:
                children:
                    - PushButton:
                        label: Add layer
                        tooltip: Add new layer
                        width: 100
    '''
    
    layer_structure = '''
    VerticalLayout:
        name: layer
        bg_color: [0.3, 0.3, 0.3]
        children:
            - HorizontalLayout:
                children:
                    - ToggleButton:
                        name: layer_number
                        width: 20
                    - TextBox:
                        label: Name
                        value: Layer
                        tooltip: Please enter layer name here
                        max_input_length: 40
                    - ToggleButton:
                        label: V
                        value: True
                        tooltip: Visibility
                        width: 20
                    - ToggleButton:
                        label: S
                        value: True
                        tooltip: Selectability
                        width: 20
                    - ToggleButton:
                        label: R
                        value: True
                        tooltip: Renderability
                        width: 20
                    - ToggleButton:
                        name: show_filter
                        tooltip: Show/hide filter
                        width: 80
                    - PushButton:
                        name: delete_layer
                        label: X
                        tooltip: Delete layer
                        width: 20
            - VerticalLayout:
                name: filters_container
                bg_color: [0.4, 0.4, 0.4]
                children:
                    - VerticalLayout:
                        name: filters
                        children:
                        - UIStructure:
                            name: filter_structure
                    - HorizontalLayout:
                        children:
                            - Fill:
                                width: 20
                            - PushButton:
                                label: Add filter
                                tooltip: Add new filter
                                width: 100
            - Fill:
                height: 10
    '''
    
    filter_structure = '''
    VerticalLayout:
        name: filter
        bg_color: [0.5, 0.5, 0.5]
        children:
            - HorizontalLayout:
                children:
                    - Fill:
                        width: 20
                    - Menu:
                        name: filter_type
                        label: 'Filter type %t|Data %x1|Name %x2|Group %x3' # TODO: refactor numbers out. define menu in different way???
                        value: 1
                        tooltip: Select filter type
                        width: 80
                    - TextBox:
                        name: filter_name
                        label: "Filter"
                        value: ""
                        tooltip: Enter filter clause
                        max_input_length: 40
                    - PushButton:
                        name: delete_filter
                        label: X
                        tooltip: Delete filter
                        width: 20
                    - Fill:
                        width: 20
            - Fill:
                height: 10
    '''

hotkeys = '''
q: quit_script
'''

class Events(AllMethodsStatic):
    def layer_number(elem):
        layer_number = int(elem.name)
        visible_layers = Window.ViewLayers()
        
        if layer_number in visible_layers:
            if len(visible_layers) > 1:
                visible_layers.remove(layer_number)
        else:
            visible_layers.append(layer_number)
        
        Window.ViewLayers(visible_layers)
    
    def add_layer(elem):
        root = elem.find_root()
        layers = root.find_child(name='layers')
        
        root_structure = unserialize(UIStructure, UIStructure.layer_structure)
        layers.append(root_structure)
    
    def delete_layer(elem):
        layers = elem.find_parent(name='layers')
        layer = elem.find_parent(name='layer')
        layers.remove(layer)
    
    def add_filter(elem):
        filters_container = elem.find_parent(name='filters_container')
        filters = filters_container.find_child(name='filters')
        root_structure = unserialize(UIStructure, UIStructure.filter_structure)
        filters.append(root_structure)
    
    def delete_filter(elem):
        filters = elem.find_parent(name='filters')
        filter = elem.find_parent(name='filter')
        filters.remove(filter)
    
    def root_container_up(root_elem):
        elem.x += 20
    
    def root_container_down(root_elem):
        elem.x -= 20
    
    def root_container_left(root_elem):
        elem.y -= 20
    
    def root_container_right(root_elem):
        elem.y += 20
    
    def quit_script(elem):
        Draw.Exit()

class Constraints(AllMethodsStatic):
    def layer_number_constraint(root_elem):
        ''' priority=1 '''
        layers = root_elem.find_child(name='layers')
        
        prev_layer_number = None
        
        for i, layer in enumerate(layers.children):
            layer_number_elem = layer.find_child(name='layer_number')
            layer_number = 0
            
            if layer_number_elem.label:
                layer_number = int(layer_number_elem.label)
            
            if layer_number != i + 1:
                layer_number_elem.label = str(i + 1)
        
        # TODO: add check for upper limit (19 is max, if it goes to 20, get rid of that layer!)
    
    def layer_number_selection_status_constraint(root_elem):
        layers = root_elem.find_child(name='layers')
        view_layers = Window.ViewLayers()
        
        for i, layer in enumerate(layers.children):
            layer_number_elem = layer.find_child(name='layer_number')
            layer_number_elem.value = i + 1 in view_layers 
    
    def show_filter_name_constraint(root_elem):
        def set_show_filter_label(filters_parent, label):
            layer = filters_parent.find_parent(name='layer')
            show_filter = layer.find_child(name='show_filter')
            show_filter.label = label
        
        layers = root_elem.find_child(name='layers')
        
        for layer in layers.children:
            filters = layer.find_child(name='filters')
            label = 'Show filter'
            
            if len(filters.children) > 1:
                label += 's'
            
            set_show_filter_label(filters, label)
    
    def filter_visibility_constraint(root_elem):
        layers = root_elem.find_child(name='layers')
        
        for layer in layers.children:
            show_filter = layer.find_child(name='show_filter')
            filters = layer.find_child(name='filters_container')
            filters.visible = show_filter.value
    
    def layer_objects_constraint(root_elem):
        object_filter = ObjectFilter(scene=Scene.GetCurrent())
        layers = root_elem.find_child(name='layers')
        
        assign_all_objects_to_layer(layer=20)
        
        for layer in layers.children:
            filtered_objects = None
            filters = layer.find_child(name='filters')
            layer_number = layer.find_child(name='layer_number')
            
            for child in filters.children:
                if child.name == 'filter':
                    filter_type = child.find_child(name='filter_type')
                    filter_name = child.find_child(name='filter_name')
                    
                    if filter_type.value == 1:
                        print 'filter data'
                        filtered_objects = object_filter.data(filter_name.value)
                    if filter_type.value == 2:
                        print 'filter name. TO BE IMPLEMENTED'
                        #filtered_objects = object_filter.name_is(filter_name.value)
                    if filter_type.value == 3:
                        print 'filter group. TO BE IMPLEMENTED'
            
            try:
                for ob in filtered_objects:
                    layers = ob.layers
                    layers.append(int(layer_number.label))
                    ob.layers = layers
            except TypeError:
                pass

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events, Constraints)
    app.run()
