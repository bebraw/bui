# -*- coding: utf-8 -*-
from bui.backend.container.horizontal import HorizontalContainer
from bui.backend.container.vertical import VerticalContainer
from bui.backend.element.fill import Fill

from bui.utils.parser import read_yaml

def unserialize(document_container, root_structure=None):
    def construct_hierarchy(current_object, document_container):
        object_args = current_object.args
        
        if object_args.has_key('children'):
            for child in object_args['children']:
                class_name = child.keys()[0]
                class_args = child.values()[0]
                
                if class_name == 'UIStructure':
                    document_name = class_args['name']
                    document_root = getattr(document_container, document_name)
                    structure = read_yaml(document_root)
                    root_object = structure.items()[0]
                    class_name = root_object[0]
                    class_args = root_object[1]
                
                class_instance = globals()[class_name]()
                
                # store args so they can be used later when constructing details
                class_instance.args = class_args
                
                current_object.append(class_instance)
                
                construct_hierarchy(class_instance, document_container)
    
    def construct_details(current_object):
        if hasattr(current_object, 'children'):
            for child in current_object.children:
                construct_details(child)
        
        if current_object.args.has_key('children'):
            del current_object.args['children']
        
        current_object.initialize(**current_object.args)
        del current_object.args
    
    document_root = root_structure or document_container.root_structure
    
    structure = read_yaml(document_root)
    
    root_object_name = structure.keys()[0]
    root_object_args = structure.values()[0]
    root_object = globals()[root_object_name]()
    root_object.args = root_object_args
    
    construct_hierarchy(root_object, document_container)
    construct_details(root_object)
    
    return root_object
