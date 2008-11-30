# -*- coding: utf-8 -*-
from bui.application import BaseApplication
from bui.container import VerticalContainer

from structure import StructureWithVerticalContainerChild

def test_create_application():
    app = BaseApplication(StructureWithVerticalContainerChild, '')
    #assert file_content is None
