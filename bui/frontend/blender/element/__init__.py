# -*- coding: utf-8 -*-

# see __init__.py in pyopengl frontend for duplicate!

# TODO: it might be nicer to use inspect module for this
# see http://ginstrom.com/scribbles/2007/10/24/python-introspection-with-the-inspect-module/

# TODO: make this dynamic if possible
# 'normal',
module_names = ('button', 'colorpicker', 'icon', 'image', 'label', 'menu', \
                'number', 'separator', 'slider', 'textbox')

serializer = __import__('bui.backend.serializer', globals(), locals(), 'bui')

for module_name in module_names:
    module = __import__(module_name, globals(), locals())

    for var_name, var_item in vars(module).items():
        if type(var_item) == type:
            setattr(serializer, var_name, var_item)
