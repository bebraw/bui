# -*- coding: utf-8 -*-
from bui.backend.application import BaseApplication
from bui.backend.container.vertical import VerticalContainer

from ..structure import StructureWithVerticalContainerChild

def test_create_application():
    app = BaseApplication(StructureWithVerticalContainerChild, '')
    #assert file_content is None
