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
        - Fill:
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

structure_with_fill_elements = '''
VerticalContainer:
    width: 200
    children:
        - Fill:
            width: 100
        - Fill:
            width: 50
'''

structure_for_event_tests = '''
VerticalContainer:
    width: 200
    children:
        - Fill:
            name: Add monkey
            width: 40
        - Fill:
            name: Add giraffe
            width: 20
        - Fill:
            name: Delete animals
            event_handler: delete_all
        - Fill:
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
        - Fill:
            height: 10
        - HorizontalContainer:
            name: last_hori
            children:
                - PushButton:
                    name: Do something
                    tooltip: Add some tool here
                    width: 100
'''

fill_element = '''
Fill:
    width: 100
'''

structure_keys = '''
a: add_monkey
d: delete_all
s:
    press: press_s
    release: release_s
'''
