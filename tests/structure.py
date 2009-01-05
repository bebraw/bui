# -*- coding: utf-8 -*-

class fsdf():
    root_structure = '''
    VerticalLayout:
        name: root_vertical
        bg_color: [0.2, 0.5, 0.6]
        width: auto
        children:
            - VerticalLayout:
                children:
                    - Label:
                        label: Some label
    '''

class StructureWithUIStructure():   
    root_structure = '''
    VerticalLayout:
        width: 300
        children:
            - UIStructure:
                name: minimal_structure
            - Fill:
                width: 80
    '''
    
    minimal_structure = '''
    VerticalLayout:
        width: 400
    '''

class MinimalStructure():
    root_structure = '''
    VerticalLayout:
        width: 400
    '''

class StructureWithHiddenVerticalLayoutChild(): 
    root_structure = '''
    VerticalLayout:
        width: 200
        children:
            - VerticalLayout:
                name: foobar
                visible: False
                width: 300
                children:
                    - Fill:
                        name: barbar
    '''

class StructureForEventTests():
    root_structure = '''
    VerticalLayout:
        width: 200
        children:
            - Fill:
                name: Add monkey
                width: 40
            - Fill:
                name: Add giraffe
                width: 20
            - Fill:
                name: delete_all
                label: Delete animals # FIXME: probably doesn't work as Fill doesn't have label!
            - Fill:
                name: add_to_ui_structure
    '''

class StructureForStateEventTests():
    root_structure = '''
    VerticalLayout:
        width: 200
        children:
            - Fill:
                name: Print foo elem
                width: 40
                events:
                    on_mouse_over: print_foo
    '''

class MultipleVerticalLayouts():
    root_structure = '''
    VerticalLayout:
        width: 200
        children:
            - VerticalLayout:
                width: 50
                children:
                    - Fill:
                        name: foo
                    - Fill:
                        name: bar
                    - Fill:
                        name: foofoo
            - VerticalLayout:
                children:
                    - Fill:
                        name: cat
                    - Fill:
                        name: dog
                    - Fill:
                        name: elephant
                    - Fill:
                        name: snake
    '''

class HiddenRootLayout():
    root_structure = '''
    VerticalLayout:
        visible: False
        width: 300
        children:
            - VerticalLayout:
                children:
                    - HorizontalLayout:
                        children:
                            - Fill:
                                name: foobar
                            - Fill:
                                name: foo
                            - Fill:
                                name: barfoo
    '''

class FillElement():
    root_structure = '''
    Fill:
        width: 100
    '''

class StructureWithAutoWidth():
    root_structure = '''
    VerticalLayout:
        width: auto
        children:
            - Fill:
                name: filler
            - Fill:
                name: another filler
                width: 50
    '''

class StructureWithFreeLayout():
    root_structure = '''
    FreeLayout:
        children:
            - Fill:
                name: first fill
            - Fill:
                name: second fill
                x: 40
                y: 500
            - Fill:
                name: third fill
                width: 800
                height: 800
    '''

class StructureWithHorizontalLayoutNoChildrenWidths():
    root_structure = '''
    HorizontalLayout:
        height: 400
        element_height: 500
        width: 100
        children:
            - Fill:
                name: first fill
            - Fill:
                name: second fill
    '''

class StructureWithHorizontalLayoutChildrenWidths():
    root_structure = '''
    HorizontalLayout:
        width: 200
        children:
            - Fill:
                name: first fill
                width: 30
            - Fill:
                name: second fill
                width: 80
    '''

class StructureWithHorizontalLayoutPartialChildrenWidths():
    root_structure = '''
    HorizontalLayout:
        width: 300
        children:
            - Fill:
                name: first fill
                width: 120
            - Fill:
                name: second fill
    '''

structure_keys = '''
a: add_monkey
d: delete_all
s:
    press: press_s
    release: release_s
'''
