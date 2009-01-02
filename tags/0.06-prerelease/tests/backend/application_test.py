# -*- coding: utf-8 -*-
from bui.backend.application import BaseApplication
from ..structure import StructureWithHiddenVerticalLayoutChild

def test_create_application():
    app = BaseApplication(StructureWithHiddenVerticalLayoutChild, '')
    #assert file_content is None
