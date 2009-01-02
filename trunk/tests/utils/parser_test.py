# -*- coding: utf-8 -*-
from bui.utils.parser import read_yaml
from ..structure import structure_with_one_item, structure_with_tabs

def test_read_invalid_file():
    file_content = read_yaml('foo.yaml')
    assert file_content is None

def test_read_valid_file():
    # IMPORTANT! Note that this passes only if py.test is ran at the tests directory.
    file_content = read_yaml('valid.yaml') 
    assert file_content == {'a': 1, 'b': {'c': 5, 'd': 4, }, }

def test_read_non_file_structure():
    structure_content = read_yaml(structure_with_one_item)
    assert structure_content == [{'some_item': None}]

def test_read_structure_with_tabs():
    structure_content = read_yaml(structure_with_tabs)
    assert structure_content == {'some_item': {'children': ['other_item', 'third_item']}}