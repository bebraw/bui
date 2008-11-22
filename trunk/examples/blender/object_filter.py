# -*- coding: utf-8 -*-
from Blender import Scene

class ObjectFilter():
    def __init__(self, scene=None, objects=None):
        self.scene = None
        self.objects = None
        
        try:
            self.scene = Scene.Get(scene)
            self.objects = self.scene.objects
        except (NameError, TypeError):
            pass
        
        if type(scene) == type(Scene.GetCurrent()):
            self.scene = scene
        
        if objects:
            self.objects = objects

    def __iter__(self):
        if self.objects:
            return self.objects.__iter__()

    def data(self, *data_types):
        objects = [object for object in self.scene.objects \
                          for data_type in data_types \
                          if object.type.lower() == data_type.lower()]
        
        return ObjectFilter(self.scene, objects)

    def _filter_objects_based_on_name(self, fragment, func):
        if self.objects and fragment:
            return [object for object in self.objects if func(object.name, fragment)]

    def name_begins_with(self, fragment):
        startswith = lambda string, fragment: string.startswith(fragment)
        return self._filter_objects_based_on_name(fragment, startswith)

    def name_ends_with(self, fragment):
        endswith = lambda string, fragment: string.endswith(fragment)
        return self._filter_objects_based_on_name(fragment, endswith)

    def name_contains(self, fragment):
        contains = lambda string, fragment: string.find(fragment) >= 0
        return self._filter_objects_based_on_name(fragment, contains)

    def name_is(self, fragment):
        check_name = lambda string, fragment: string == fragment
        return self._filter_objects_based_on_name(fragment, check_name)
