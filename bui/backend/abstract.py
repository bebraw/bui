# -*- coding: utf-8 -*-
from bui.utils.attribute import set_attributes_based_on_kvargs
from render import RenderNode

class AbstractObject(object):
    def __init__(self, **kvargs):
        super(AbstractObject, self).__init__(**kvargs)
        
        self.name = ''
        self.tooltip = ''
        
        # TODO: check if this should be here! -> to event stuff???
        self.events = []
        self.event_index = 0
        
        set_attributes_based_on_kvargs(self, **kvargs)
        
        self.render_node = RenderNode(**kvargs)
    
    def render(self):
        self.render_node.render()
