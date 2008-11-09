# -*- coding: utf-8 -*-
from parser import parse_structure

class Serializer(object):
    def __init__(self, namespace):
        self.namespace = namespace
    
    def serialize(self, structure):
        return parse_structure(structure, self.namespace)
