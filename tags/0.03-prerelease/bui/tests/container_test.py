# -*- coding: utf-8 -*-
from bui.container import *

class TestFill():
    def test_render(self):
        container = Fill()
        #container.render(None) # need to pass real coord here
        # assert that coord has not changed

class TestHorizontalContainer():
    def test_render(self):
        container = HorizontalContainer()
        #container.render(None) # need to pass real coord here
        # assert the change of coord

class TestVerticalContainer():
    def test_render(self):
        container = VerticalContainer()
        #container.render(None) # need to pass real coord here
        # assert the change of coord
