# -*- coding: utf-8 -*-
from bui.backend.container.abstract import AbstractContainer
from bui.backend.serializer import unserialize

from ..structure import MinimalStructure

# TODO: move append test to tree util tests!
class TestAbstractContainer():
    def test_append(self):
        abstract_container = AbstractContainer()
        
        structure_root = unserialize(MinimalStructure())
        abstract_container.append(structure_root)
        
        assert len(abstract_container.children) == 1
        assert abstract_container.children[0].width == 400
        assert abstract_container.children[0].parent == abstract_container
