# -*- coding: utf-8 -*-
from bui.backend.serializer import unserialize
from bui.utils.attribute import AttributeSetter, BooleanAttribute, IntegerAttribute, StringAttribute
from bui.utils.errors import ValueMissingError
from bui.utils.parser import read_yaml
from bui.utils.tree import TreeChild, TreeParent
from constraint import BaseConstraintManager
from event import BaseEventManager
from timer import BaseTimerManager
from serializer import unserialize

# TODO: should use a list based scheme to determine conf item names, types, min, max etc.
# to make testing easier

# this class should handle global constraints/events/timers!
class BaseWindowManager(AttributeSetter):
    def __init__(self, configuration, structure_document=None, hotkeys=None, events=None,
                 timers=None, constraints=None, initializers=None):
        # TODO: should handle both global and local constraints. move part to Window level?
        #self.constraint_manager = BaseConstraintManager(self.root_layout, constraints)
        # how about event manager? should there be one for global events???
        
        #self.windows = BaseWindowContainer(configuration, structure, hotkeys, events,
        #                                   timers, constraints, initializers)
        
        self.name = StringAttribute(value='')
        self.label = StringAttribute(value='')
        self.width = IntegerAttribute(value=1, min=1, max=10000)
        self.height = IntegerAttribute(value=1, min=1, max=10000)
        self.full_screen = BooleanAttribute(value=False)
        self.v_sync = BooleanAttribute(value=False)
        self.show_fps = BooleanAttribute(value=False)
        self.logging = BooleanAttribute(value=False)
        self.alignment = StringAttribute(value='center')
        self.element_height = IntegerAttribute(value=1, min=1, max=10000)
        self.start_timers = BooleanAttribute(value=False)
        
        self.structure = None
        
        self.hotkeys = None
        self.initializer = None
        
        self.parse_configuration(configuration)
        
        self.structure_document = structure_document
        if self.structure_document and self.structure:
            self.structure = getattr(self.structure_document, self.structure)
        
        if self.hotkeys:
            self.hotkeys = getattr(hotkeys, self.hotkeys)
        
        if self.initializer:
            self.initializer = getattr(initializers, self.initializer)
        
        if not self.width:
            raise ValueMissingError, 'Missing width!'
        
        if not self.height:
            raise ValueMissingError, 'Missing height!'
        
        self.timers = timers
        
        self.initialize_windows()
        self.initialize_timers()
    
    def parse_configuration(self, configuration):
        parsed_configuration = read_yaml(configuration)
        
        for item, value in parsed_configuration.items():
            if self.__dict__.has_key(item):
                self.__dict__[item] = value
    
    def initialize_timers(self):
        pass # TODO: add tests and dummy BaseTimerManager
    
    def initialize_windows(self):
        # XXX: just one window for now
        self.windows = []
        self.windows.append(BaseWindow(self.name, self.label, self.width, self.height,
                                       self.show_fps, self.logging, self.alignment,
                                       self.element_height, self.start_timers,
                                       self.structure_document, self.structure, self.hotkeys,
                                       self.initializer))
        
        #self.windows = BaseWindowContainer(...)
    
    def redraw(self):
        # TODO: clarify the way constraints are handled!
        #self.constraint_manager.check_constraints()
        self.windows[0].redraw() # evil hack
    
    def run(self):
        # XXX: supports only one window for now
        if len(self.windows) > 0:
            # FIXME: timers should be per window! (how about global timers??? are timers always per window or are they always global?)
            if self.start_timers:
                self.timer_manager.start()
            
            self.windows[0].run()
        #self.windows.run()

class BaseWindowContainer(list):
    def __init__(self, configuration, structure, hotkeys=None, events=None,
                 timers=None, constraints=None, initializers=None):
        pass
        # should initialize windows now using configuration!
        # self.append(Window(layout, name, width, height, hotkeys, events, timers, constraints, initializer)
    
    def redraw(self):
        for window in self:
            window.render()
    
    def run(self):
        for window in self:
            window.run()

# note that this should be easy to extend!!!
class BaseWindow(TreeChild, TreeParent):
    def __init__(self, name, label, width, height, show_fps, logging, alignment,
                 element_height, start_timers, structure_document, structure,
                 hotkeys, initializer):
        super(BaseWindow, self).__init__()
        
        self.name = name
        self.label = label
        self.width = width
        self.height = height
        self.show_fps = show_fps
        self.logging = logging
        self.alignment = alignment
        self.element_height = element_height
        self.start_timers = start_timers
        self.hotkeys = hotkeys
        self.initializer = initializer
        #self.initializer = UserInterfaceInitializer(initializer)
        self.root_layout = None #EmptyLayout() # better to use AbstractObject instead???
        
        # TODO: move this test to unserialize???
        if structure_document and structure:
            self.root_layout = unserialize(structure_document, structure)
            self.root_layout.parent = self
            self.children.append(self.root_layout)
            # could use self.append also but i think this is neater as it's explicit
            # TODO: check this out
        else:
            # TODO: should give nice warning (or just use assert?)
            print structure_document, structure
        
        # note that should also provide info about which structure to use if not default (set in config!)
        # figure out how to handle keys and events (active context!!!)
        #self.event_manager = BaseEventManager(self.root_layout, keys, events)
        #self.constraint_manager
    
    def redraw(self):
        self.root_layout.render()
    
    def run(self):
        if self.initializer: # TODO: get rid of if
            self.initializer.run(self.root_layout, self.timer_manager)
    
    # TODO: get rid of this?
    #def update_structure(self):
        # nasty hack as the updates are not nice yet
        #if hasattr(self, 'event_manager'): # get rid of hasattr???
        #self.event_manager.construct_element_event_ids(self.root_layout)
    
    def get_height(self):
        return self._height
    def set_height(self, height):
        self._height = max(height, 1)
    height = property(get_height, set_height)
    
    def get_width(self):
        return self._width
    def set_width(self, width):
        self._width = max(width, 1)
    width = property(get_width, set_width)

class EmptyLayout(object):
    def render(self):
        pass

class UserInterfaceInitializer(object):
    def __init__(self, func=None):
        self.func = None
        
        if hasattr(func, '__call__'):
            self.func = func
    
    def run(self, root_layout, timer_manager):
        if self.func:
            self.func(root_layout, timer_manager)
