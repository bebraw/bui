# -*- coding: utf-8 -*-

try:
    from Blender import Draw
except ImportError:
    pass

from bui.element import AbstractElement

class AbstractBlenderElement(AbstractElement):
    suitable_values = ('name', 'width', 'height', 'tooltip', 'value', 'max_input_length', 'event_handler', 'variable', 'min', 'max', 'range', 'precision') # TODO: refactor
    
    def __init__(self, args=None):
        self.name = ''
        self.event = 0
        self.tooltip = ''
        self.value = 0.0
        self.max_input_length = 0
        self.min = 0.0
        self.max = 1.0
        #self.width = 0
        #self.height = 0
        self.range = 0 # no clickstep
        self.precision = 0.0 # 4 decimals
        super(AbstractBlenderElement, self).__init__(args)
    
    def update_value(self, evt, val):
        self.value = val

class Label(AbstractBlenderElement):
    def render(self, coord):
        self.label = Draw.Label(self.name, coord.x, coord.y, self.width, self.height)

class TextBox(AbstractBlenderElement):
    def render(self, coord):
        self.textbox = Draw.String(self.name + ':', self.event, coord.x, coord.y, self.width, self.height,
                              self.value, self.max_input_length, self.tooltip, self.update_value)

class ToggleButton(AbstractBlenderElement):
    def render(self, coord):
        self.togglebutton = Draw.Toggle(self.name, self.event, coord.x, coord.y, self.width, self.height,
                                   self.value, self.tooltip, self.update_value)

class PushButton(AbstractBlenderElement):
    def render(self, coord):
        self.pushbutton = Draw.PushButton(self.name, self.event, coord.x, coord.y, self.width,
                                          self.height, self.tooltip)

class Menu(AbstractBlenderElement):
    def render(self, coord):
        self.menu = Draw.Menu(self.name, self.event, coord.x, coord.y, self.width, self.height,
                         self.value, self.tooltip, self.update_value)

class Slider(AbstractBlenderElement):
    def render(self, coord):
        self.slider = Draw.Slider(self.name, self.event, coord.x, coord.y, self.width, self.height,
                                  self.value, self.min, self.max, False, self.tooltip, self.update_value)

class Number(AbstractBlenderElement):
    def render(self, coord):
        try:
            self.number = Draw.Number(self.name, self.event, coord.x, coord.y, self.width, self.height,
                                  self.value, self.min, self.max, self.tooltip, self.update_value, self.range, self.precision)
        except: # needed for backwards compatibility (no range and precision in 2.48a)
            self.number = Draw.Number(self.name, self.event, coord.x, coord.y, self.width, self.height,
                                  self.value, self.min, self.max, self.tooltip, self.update_value)

class IntNumber(AbstractBlenderElement):
    def render(self, coord):
        self.number = Draw.Number(self.name, self.event, coord.x, coord.y, self.width, self.height,
                                  int(self.value), int(self.min), int(self.max), self.tooltip, self.update_value)