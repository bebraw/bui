# -*- coding: utf-8 -*-
from bui.backend.application import BaseApplication
from bui.backend.container import VerticalContainer

from bui.tests.structure import StructureWithVerticalContainerChild

def test_create_application():
    app = BaseApplication(StructureWithVerticalContainerChild, '')
    #assert file_content is None
