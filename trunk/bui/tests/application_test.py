# -*- coding: utf-8 -*-
from bui.application import Application

test_structure = '''
VerticalContainer:
    width: 400
'''

def test_create_application():
    app = Application(test_structure, globals())
    #assert file_content is None
