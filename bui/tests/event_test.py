# -*- coding: utf-8 -*-
from bui.abstract import AbstractContainer
from bui.event import EventManager

class TestEventManager():
    def test_create_event_manager(self):
        self.event_manager = EventManager(root_container=AbstractContainer(globals()), element_height=20)
