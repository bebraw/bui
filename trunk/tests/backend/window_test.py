# -*- coding: utf-8 -*-
from bui.backend.layout import VerticalLayout
from bui.backend.window import BaseWindowManager
from bui.utils.errors import ValueMissingError
from bui.utils.test import raises
from ..hotkeys import SimpleHotkeys
from ..initializers import SimpleInitializers
from ..structure import StructureWithUIStructure

# TODO: test run()

class TestSingleWindowApplication():
    def test_load_empty_window_configuration(self):
        def create_window_manager():
            window_manager = BaseWindowManager('')
        
        raises(ValueMissingError, 'Missing width!', create_window_manager)
    
    def test_load_window_configuration_only_with_width(self):
        def create_window_manager():
            window_manager = BaseWindowManager('width: 400')
        
        raises(ValueMissingError, 'Missing height!', create_window_manager)
    
    only_valid_width_and_height = '''
        width: 400
        height: 200
    '''
    def test_load_window_configuration_with_valid_width_and_height(self):
        window_manager = BaseWindowManager(self.only_valid_width_and_height)
        
        # check what the window manager itself looks like
        assert window_manager.name == ''
        assert window_manager.label == ''
        assert window_manager.width == 400
        assert window_manager.height == 200
        assert window_manager.full_screen == False
        assert window_manager.v_sync == False
        assert window_manager.show_fps == False
        assert window_manager.logging == False
        assert window_manager.alignment == 'center'
        assert window_manager.element_height == 0
        assert window_manager.start_timers == False
        assert window_manager.structure == None
        assert window_manager.hotkeys == None
        assert window_manager.initializer == None
        
        # check the window itself (TODO: use window_manager.window alias in this case???)
        # note that window doesn't have all attributes of a window manager!
        window = window_manager.windows[0]
        assert window.name == ''
        assert window.label == ''
        assert window.width == 400
        assert window.height == 200
        assert window.show_fps == False
        assert window.logging == False
        assert window.alignment == 'center' # defined only initially and used on window creation. should this be retained?
        assert window.element_height == 0
        assert window.start_timers == False # same thing as with alignment!
        assert window.root_layout == None
        assert window.hotkeys == None
        assert window.initializer == None # same thing as with alignment! used only on run!
    
    all_possible_settings_set_as_valid = '''
        name: test_application
        label: Test application
        width: 300
        height: 600
        full_screen: True
        v_sync: True
        show_fps: True
        logging: True
        alignment: 'right'
        element_height: 50
        start_timers: True
        structure: minimal_structure # TODO: rename layout to structure or vice versa?
        hotkeys: hotkeys
        initializer: simple_initializer
    '''
    
    def test_load_window_configuration_with_all_possible_settings_set_as_valid(self):
        window_manager = BaseWindowManager(self.all_possible_settings_set_as_valid,
                                           structure_document=StructureWithUIStructure,
                                           hotkeys=SimpleHotkeys,
                                           initializers=SimpleInitializers)
        
        assert window_manager.name == 'test_application'
        assert window_manager.label == 'Test application'
        assert window_manager.width == 300
        assert window_manager.height == 600
        assert window_manager.full_screen == True
        assert window_manager.v_sync == True
        assert window_manager.show_fps == True
        assert window_manager.logging == True
        assert window_manager.alignment == 'right'
        assert window_manager.element_height == 50
        assert window_manager.start_timers == True
        assert window_manager.structure == StructureWithUIStructure.minimal_structure
        assert window_manager.hotkeys == SimpleHotkeys.hotkeys
        assert window_manager.initializer == SimpleInitializers.simple_initializer
        
        # check the window itself (TODO: use window_manager.window alias in this case???)
        # note that window doesn't have all attributes of a window manager!
        window = window_manager.windows[0]
        assert window.name == 'test_application'
        assert window.label == 'Test application'
        assert window.width == 300
        assert window.height == 600
        assert window.show_fps == True
        assert window.logging == True
        assert window.alignment == 'right' # defined only initially and used on window creation. should this be retained?
        assert window.element_height == 50
        assert window.start_timers == True # same thing as with alignment!
        assert window.hotkeys == SimpleHotkeys.hotkeys
        assert window.initializer == SimpleInitializers.simple_initializer # same thing as with alignment! used only on run!
        
        assert isinstance(window.root_layout, VerticalLayout)
    
    # TODO: test alignment options (left, right, top, bottom, center, topleft, etc.)
    # TODO: test invalid cases
