# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractObject

from bui.utils.tree import TreeParent

# TODO: this class becomes redundant if event updates are changed to use observers!

class AbstractContainer(TreeParent, AbstractObject):
    def append(self, abstract_object):
        super(AbstractContainer, self).append(abstract_object)
        
        # get rid of this? how to update events?
        if hasattr(self.common, 'application'):
            self.common.application.update_structure()
    
    def remove(self, abstract_object):
        super(AbstractContainer, self).remove(abstract_object)
        
        # get rid of this? how to update events?
        if hasattr(self.common, 'application'):
            self.common.application.update_structure()
