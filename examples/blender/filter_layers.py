# -*- coding: utf-8 -*-
from Blender import Draw, Scene, Window

from bui.blender.application import Application
from bui.serializer import unserialize

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

# ------------------- UTILS ---------------------------
def clamp(val, min_val, max_val):
    return min(max(val, min_val), max_val)

def assign_all_objects_to_layer(layer):
    scn = Scene.GetCurrent()
    
    for ob in scn.objects:
        ob.layers = [layer, ]

class UIStructure():
    root_structure = '''
    VerticalContainer:
        width: 400
        children:
            - HorizontalContainer:
                children:
                    - Label:
                        name: Filter layers v0.9
                    - PushButton:
                        name: X
                        tooltip: Quit script
                        event_handler: quit_script
                        width: 20
            - Fill:
                height: 10
            - VerticalContainer:
                name: layers
                children:
                    - UIStructure:
                        name: layer_structure
            - HorizontalContainer:
                children:
                    - PushButton:
                        name: Add layer
                        tooltip: Add new layer
                        width: 100
    '''
    
    layer_structure = '''
    VerticalContainer:
        name: layer
        children:
            - HorizontalContainer:
                children:
                    - ToggleButton:
                        variable: layer_number
                        event_handler: toggle_layer_number
                        width: 20
                    - TextBox:
                        name: Name
                        value: Layer
                        tooltip: Please enter layer name here
                        max_input_length: 40
                    - ToggleButton:
                        name: V
                        value: True
                        tooltip: Visibility
                        width: 20
                    - ToggleButton:
                        name: S
                        value: True
                        tooltip: Selectability
                        width: 20
                    - ToggleButton:
                        name: R
                        value: True
                        tooltip: Renderability
                        width: 20
                    - ToggleButton:
                        variable: show_filter
                        tooltip: Show/hide filter
                        width: 80
                    - PushButton:
                        name: X
                        tooltip: Delete layer
                        event_handler: delete_layer
                        width: 20
            - VerticalContainer:
                name: filters_container
                children:
                    - VerticalContainer:
                        name: filters
                        children:
                        - UIStructure:
                            name: filter_structure
                    - HorizontalContainer:
                        children:
                            - Fill:
                                width: 20
                            - PushButton:
                                name: Add filter
                                tooltip: Add new filter
                                width: 100
            - Fill:
                height: 10
    '''
    
    filter_structure = '''
    VerticalContainer:
        name: filter
        children:
            - HorizontalContainer:
                children:
                    - Fill:
                        width: 20
                    - Menu:
                        name: 'Filter type %t|Data %x1|Name %x2|Group %x3' # TODO: refactor numbers out. define menu in different way???
                        value: 1
                        variable: filter_type
                        tooltip: Select filter type
                        width: 80
                    - TextBox:
                        name: "Filter"
                        value: ""
                        variable: filter_name
                        tooltip: Enter filter clause
                        max_input_length: 40
                    - PushButton:
                        name: X
                        tooltip: Delete filter
                        event_handler: delete_filter
                        width: 20
                    - Fill:
                        width: 20
            - Fill:
                height: 10
    '''

hotkeys = '''
q: quit_script
'''

class Events():
    @staticmethod
    def toggle_layer_number(elem):
        layer_number = int(elem.name)
        visible_layers = Window.ViewLayers()
        
        if layer_number in visible_layers:
            if len(visible_layers) > 1:
                visible_layers.remove(layer_number)
        else:
            visible_layers.append(layer_number)
        
        Window.ViewLayers(visible_layers)
    
    @staticmethod
    def add_layer(elem):
        root = elem.find_root_element()
        layers = root.find_child(name='layers')
        root_structure = unserialize(UIStructure, UIStructure.layer_structure)
        layers.add_child_structure(root_structure)
    
    @staticmethod
    def delete_layer(elem):
        layers = elem.find_parent(name='layers')
        layer = elem.find_parent(name='layer')
        layers.children.remove(layer)
    
    @staticmethod
    def add_filter(elem):
        filters_container = elem.find_parent(name='filters_container')
        filters = filters_container.find_child(name='filters')
        root_structure = unserialize(UIStructure, UIStructure.filter_structure)
        filters.add_child_structure(root_structure)
    
    @staticmethod
    def delete_filter(elem):
        filters = elem.find_parent(name='filters')
        filter = elem.find_parent(name='filter')
        filters.children.remove(filter)
    
    @staticmethod
    def root_container_up(root_elem):
        elem.x_offset += 20
    
    @staticmethod
    def root_container_down(root_elem):
        elem.x_offset -= 20
    
    @staticmethod
    def root_container_left(root_elem):
        elem.y_offset -= 20
    
    @staticmethod
    def root_container_right(root_elem):
        elem.y_offset += 20
    
    @staticmethod
    def quit_script(elem):
        Draw.Exit()

class Constraints():
    @staticmethod
    def layer_number_constraint(root_elem):
        '''priority=1'''
        layers = root_elem.find_child(name='layers')
        
        prev_layer_number = None
        
        for i, layer in enumerate(layers.children):
            layer_number_elem = layer.find_child(variable='layer_number')
            layer_number = 0
            
            if layer_number_elem.name:
                layer_number = int(layer_number_elem.name)
            
            if layer_number != i + 1:
                layer_number_elem.name = str(i + 1)
        
        # TODO: add check for upper limit (19 is max, if it goes to 20, get rid of that layer!)
    
    @staticmethod
    def layer_number_selection_status_constraint(root_elem):
        layers = root_elem.find_child(name='layers')
        view_layers = Window.ViewLayers()
        
        for i, layer in enumerate(layers.children):
            layer_number_elem = layer.find_child(variable='layer_number')
            layer_number_elem.value = i + 1 in view_layers 
    
    @staticmethod
    def show_filter_name_constraint(root_elem):
        def set_show_filter_name(filters_parent, name):
            layer = filters_parent.find_parent(name='layer')
            show_filter = layer.find_child(variable='show_filter')
            show_filter.name = name
        
        layers = root_elem.find_child(name='layers')
        
        for layer in layers.children:
            filters = layer.find_child(name='filters')
            name = 'Show filter'
            
            if len(filters.children) > 1:
                name += 's'
        
            set_show_filter_name(filters, name)
    
    @staticmethod
    def filter_visibility_constraint(root_elem):
        layers = root_elem.find_child(name='layers')
        
        for layer in layers.children:
            show_filter = layer.find_child(variable='show_filter')
            filters = layer.find_child(name='filters_container')
            filters.visible = show_filter.value
    
    @staticmethod
    def layer_objects_constraint(root_elem):
        object_filter = ObjectFilter(scene=Scene.GetCurrent())
        layers = root_elem.find_child(name='layers')
        
        assign_all_objects_to_layer(layer=20)
        
        for layer in layers.children:
            filtered_objects = None
            filters = layer.find_child(name='filters')
            layer_number = layer.find_child(variable='layer_number')
            
            for child in filters.children:
                if child.name == 'filter':
                    filter_type = child.find_child(variable='filter_type')
                    filter_name = child.find_child(variable='filter_name')
                    
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
                    layers.append(int(layer_number.name))
                    ob.layers = layers
            except TypeError:
                pass

# ----------------- INITIALIZATION -------------------
if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events, Constraints)
    app.run()
