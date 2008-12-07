# -*- coding: utf-8 -*-
from parser import read_yaml

def unserialize(document, namespace):
    def unserialize_structure(current_object, args, namespace):
        if args.has_key('children'):
            for child in args['children']:
                class_name = child.keys()[0]
                class_args = child.values()[0]
                
                if class_name == 'UIStructure':
                    structure_name = class_args['name']
                    structure = namespace[structure_name]
                    class_instance = unserialize(structure, namespace)
                else:
                    class_instance = namespace[class_name](**class_args)
                
                class_instance.parent = current_object
                current_object.children.append(class_instance)
                unserialize_structure(class_instance, class_args, namespace)
    
    structure = read_yaml(document)
    root_class_name = structure.keys()[0]
    root_class_args = structure.values()[0]
    root_object = namespace[root_class_name](**root_class_args)
    unserialize_structure(root_object, root_class_args, namespace)
    
    return root_object