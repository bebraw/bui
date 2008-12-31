# -*- coding: utf-8 -*-
from Blender import Draw
from abstract import AbstractBlenderElement

#FIXME: self.update_value callback doesn't get called for some reason -> value does not get updated
class Normal(AbstractBlenderElement):
    def initialize(self, **kvargs):
        self.value = (1.0, 1.0, 1.0, )
        super(Normal, self).initialize(**kvargs)
    
    def render(self):
        super(Normal, self).render()
        Draw.Normal(self.event, self.x, self.y, self.width,
                    self.height, self.value, self.tooltip, self.update_value)
