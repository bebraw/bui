# -*- coding: utf-8 -*-
from yaml import safe_load

def read_yaml(document):
    try:
        stream = file(document, 'r')
    except IOError:
        stream = document
        stream = stream.expandtabs(4)
    
    structure = safe_load(stream)
    
    if structure and structure != document:
        return structure
    
    return {}
