# -*- coding: utf-8 -*-
from bui.container import AbstractContainer
from bui.event import EventManager

class TestEventManager():
    def test_create_event_manager(self):
        self.event_manager = EventManager(AbstractContainer(globals()), 20, globals())
