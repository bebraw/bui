from Blender import Draw

from bui.serializer import unserialize

from bui.blender.application import Application

class UIStructure():
    root_structure = '''
    VerticalContainer:
        width: 600
        children:
            - HorizontalContainer:
                children:
                    - Label:
                        name: Amazing state event test v0.1
            - Fill:
                height: 10
            - HorizontalContainer:
                children:
                    - Image:
                        file: Mandril.png
                        height: 100
                        events:
                            on_mouse_over: show_big_image
            - HorizontalContainer:
                name: big_image
    '''
    
    image_structure = '''
    Image:
        file: Mandril.png
        width: 10
    '''

hotkeys = '''
q: quit_script
'''

class Events():
    @staticmethod
    def quit_script(elem):
        Draw.Exit()
    
    @staticmethod
    def show_big_image(root_elem):
        big_image_elem = root_elem.find_child(name='big_image')
        image_root = unserialize(UIStructure, UIStructure.image_structure)
        big_image_elem.add_child_structure(image_root)

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events)
    app.run()
