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

structure_for_event_tests = '''
VerticalContainer:
    width: 200
    children:
        - EmptyElement:
            name: Add monkey
            width: 40
        - EmptyElement:
            name: Add giraffe
            width: 20
        - EmptyElement:
            name: Delete animals
            event_handler: delete_all
        - EmptyElement:
            event_handler: add_to_ui_structure
'''

structure_for_simple_script = '''
VerticalContainer:
    name: root_vertical
    width: 400
    children:
        - HorizontalContainer:
            name: test_hori
            children:
                - Label:
                    name: Test script
                - PushButton:
                    name: X
                    tooltip: Quit script
                    event_handler: quit_script
                    width: 20
        - EmptyContainer:
            name: empty_cont
            height: 10
        - HorizontalContainer:
            name: last_hori
            children:
                - PushButton:
                    name: Do something
                    tooltip: Add some tool here
                    width: 100
'''

empty_element = '''
EmptyElement:
    width: 100
'''

structure_keys = '''
a: add_monkey
d: delete_all
'''
