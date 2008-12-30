# -*- coding: utf-8 -*-
from bui.backend.abstract import AbstractChild

from bui.utils.tree import TreeParent

class AbstractContainer(TreeParent, AbstractChild):
    def append(self, abstract_object):
        abstract_object.parent = self
        self.children.append(abstract_object)
        
        if hasattr(self.common, 'application'):
            self.common.application.update_structure()
    
    def remove(self, abstract_object):
        self.children.remove(abstract_object)
        
        if hasattr(self.common, 'application'):
            self.common.application.update_structure()
    
    #def render(self):
    #    super(AbstractContainer, self).render()
        
        #self.render_bg_color()
        
        #for child in self.children:
        #    if child.visible:
        #        child.render_bg_color()
        #        child.render()
