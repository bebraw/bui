# -*- coding: utf-8 -*-
from bui.application import Application
from bui.container import VerticalContainer

from structure import minimal_structure

def test_create_application():
    app = Application(minimal_structure, '', globals())
    #assert file_content is None
