# -*- coding: utf-8 -*-
from bui.container import VerticalContainer
from bui.parser import parse_structure, read_yaml

from structure import *

def test_read_invalid_file():
    file_content = read_yaml('foo.yaml')
    assert file_content is None

def test_read_valid_file():
    file_content = read_yaml('valid.yaml') 
    assert file_content == {'a': 1, 'b': {'c': 5, 'd': 4, }, }

def test_read_non_file_structure():
    structure_content = read_yaml(structure_with_one_item)
    assert structure_content == [{'some_item': None}]

def test_parse_valid_minimal_structure():
    root_container = parse_structure(minimal_structure, globals())
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 400

def test_parse_valid_structure_with_child_container():
    root_container = parse_structure(structure_vertical_container_child, globals())
    
    assert isinstance(root_container, VerticalContainer)
    assert root_container.width == 200
    assert len(root_container.children) == 1
    
    child_container = root_container.children[0]
    
    assert isinstance(child_container, VerticalContainer)
    assert child_container.width == 300
