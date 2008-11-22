# -*- coding: utf-8 -*-
from bui.application import Application
from bui.container import VerticalContainer

from structure import StructureWithVerticalContainerChild

def test_create_application():
    app = Application(StructureWithVerticalContainerChild, '')
    #assert file_content is None
