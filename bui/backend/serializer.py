# -*- coding: utf-8 -*-
from bui.backend.container import *
from bui.backend.element import *

from bui.utils.parser import read_yaml

def unserialize(document_container, root_structure=None):
    def unserialize_structure(document_container, current_object, args):
        if args.has_key('children'):
            for child in args['children']:
                class_name = child.keys()[0]
                class_args = child.values()[0]
                
                if class_name == 'UIStructure':
                    document_name = class_args['name']
                    document_root = getattr(document_container, document_name)
                    structure = read_yaml(document_root)
                    root_object = structure.items()[0]
                    class_name = root_object[0]
                    class_args = root_object[1]
                
                class_instance = globals()[class_name](**class_args)
                class_instance.parent = current_object
                current_object.children.append(class_instance)
                unserialize_structure(document_container, class_instance, class_args)
    
    document_root = root_structure or document_container.root_structure
    
    structure = read_yaml(document_root)
    root_class_name = structure.keys()[0]
    root_class_args = structure.values()[0]
    root_object = globals()[root_class_name](**root_class_args)
    unserialize_structure(document_container, root_object, root_class_args)
    
    return root_object
