# -*- coding: utf-8 -*-

structure_with_one_item = '''
- some_item:
'''

structure_with_tabs = '''
some_item:
	children:
		- other_item
		- third_item
'''

class StructureWithUIStructure():   
    root_structure = '''
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

class MinimalStructure():
    root_structure = '''
    VerticalContainer:
        width: 400
    '''

class StructureWithVerticalContainerChild(): 
    root_structure = '''
    VerticalContainer:
        width: 200
        children:
            - VerticalContainer:
                name: foobar
                visible: False
                width: 300
    '''

class StructureWithVerticalContainerChildren():
    root_structure = '''
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

class StructureWithHorizontalContainerChild(): 
    root_structure = '''
    VerticalContainer:
        width: 200
        children:
            - HorizontalContainer:
                height: 40
                width: 100
    '''

class StructureWithMultipleContainers():
    root_structure = '''
    VerticalContainer:
        width: 200
        children:
            - HorizontalContainer:
                width: 100
            - VerticalContainer:
                width: 150
    '''

class StructureWithFillElements():
    root_structure = '''
    VerticalContainer:
        width: 200
        children:
            - Fill:
                width: 100
            - Fill:
                width: 50
    '''

class StructureForEventTests():
    root_structure = '''
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

class StructureForStateEventTests():
    root_structure = '''
    VerticalContainer:
        width: 200
        children:
            - Fill:
                name: Print foo elem
                width: 40
                events:
                    on_mouse_over: print_foo
    '''

class StructureForSimpleScript():
    root_structure = '''
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

class FillElement():
    root_structure = '''
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
