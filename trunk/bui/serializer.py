# -*- coding: utf-8 -*-
from parser import read_yaml

def extract_class_name_and_args():
    pass

def serialize(document, namespace):
    def serialize_structure(current_object, args, namespace):
        #assert isinstance(args, dict)
        
        if args.has_key('children'):
            for child in args['children']:
                class_name = child.keys()[0]
                class_args = child.values()[0]
                
                if class_name == 'UIStructure':
                    structure_name = class_args['name']
                    structure = namespace[structure_name]
                    class_instance = serialize(structure, namespace)
                else:
                    class_instance = namespace[class_name](class_args)
                    
                class_instance.parent = current_object
                
                if hasattr(current_object, 'children'):
                    current_object.children.append(class_instance)
                else:
                    current_object.children = [class_instance, ]
                
                serialize_structure(current_object, class_args, namespace)
    
    structure = read_yaml(document)
    root_class_name = structure.keys()[0]
    root_class_args = structure.values()[0]
    
    root_object = namespace[root_class_name](root_class_args)
    
    serialize_structure(root_object, root_class_args, namespace)
    
    return root_object
