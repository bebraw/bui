# -*- coding: utf-8 -*-
from yaml import load

from container import *

'''
TODO:
-handle YAML structure seeking (import!) -> Application
'''

def read_yaml(document):
    try:
        file_stream = file(document, 'r')
    except IOError:
        file_stream = document
    
    structure = load(file_stream)
    
    return structure if structure != document else None

def parse_structure(structure):
    content = read_yaml(structure)
    root_class_name = content.keys()[0]
    root_class_args = content.values()[0]
    
    return globals()[root_class_name](root_class_args)
