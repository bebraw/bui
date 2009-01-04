# -*- coding: utf-8 -*-
from bui.utils.parser import read_yaml

def test_read_invalid_file():
    file_content = read_yaml('foo.yaml')
    assert file_content == {}

# FIXME: skip this test if not tests are not run in the right directory
def test_read_valid_file():
    file_content = read_yaml('valid.yaml') 
    assert file_content == {'a': 1, 'b': {'c': 5, 'd': 4, }, }, 'This test fails if it is run at some other directory than in which the test is!'

def test_read_empty_structure():
    structure_content = read_yaml('')
    assert structure_content == {}

structure_with_one_item = '''
- some_item:
'''
def test_read_non_file_structure():
    structure_content = read_yaml(structure_with_one_item)
    assert structure_content == [{'some_item': None}]

structure_with_tabs = '''
some_item:
	children:
		- other_item
		- third_item
'''
def test_read_structure_with_tabs():
    structure_content = read_yaml(structure_with_tabs)
    assert structure_content == {'some_item': {'children': ['other_item', 'third_item']}}
