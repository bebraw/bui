# -*- coding: utf-8 -*-

structure_with_one_item = '''
- some_item:
'''

structure_with_uistructure = '''
VerticalContainer:
    width: 300
    children:
        - UIStructure:
            name: minimal_structure
        - EmptyElement:
            width: 80
'''

minimal_structure = '''
VerticalContainer:
    width: 400
'''

structure_vertical_container_child = '''
VerticalContainer:
    width: 200
    children:
        - VerticalContainer:
            name: foobar
            visible: False
            width: 300
'''

structure_vertical_container_children = '''
VerticalContainer:
    width: 200
    children:
        - VerticalContainer:
            name: foobar
            visible: False
            width: 50
        - VerticalContainer:
            name: foobar
        - VerticalContainer:
            name: foobar
        - VerticalContainer:
            name: barbar
'''

structure_horizontal_container_child = '''
VerticalContainer:
    width: 200
    children:
        - HorizontalContainer:
            height: 40
            width: 100
'''

structure_with_multiple_containers = '''
VerticalContainer:
    width: 200
    children:
        - HorizontalContainer:
            width: 100
        - VerticalContainer:
            width: 150
'''

structure_with_empty_elements = '''
VerticalContainer:
    width: 200
    children:
        - EmptyElement:
            width: 100
        - EmptyElement:
            width: 50
'''
