# -*- coding: utf-8 -*-
from bui.container import VerticalContainer
from bui.element import EmptyElement
from bui.serializer import Serializer

from structure import minimal_structure, structure_with_uistructure

class TestSerializer():
    def test_create_serializer(self):
        serializer = Serializer(globals())
        
        root_container = serializer.serialize(structure_with_uistructure)
        assert isinstance(root_container, VerticalContainer)
