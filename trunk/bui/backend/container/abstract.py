# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractChild

from bui.utils.tree import TreeParent

class AbstractContainer(TreeParent, AbstractChild):
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
