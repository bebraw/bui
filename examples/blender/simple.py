from Blender import Draw

from bui.blender.application import BlenderApplication

class UIStructure():
    root_structure = '''
    VerticalContainer:
        name: root_vertical
        width: 400
        children:
            - HorizontalContainer:
                name: test_hori
                children:
                    - Label:
                        name: Test script
                    - PushButton:
                        name: X
                        tooltip: Quit script
                        event_handler: quit_script
                        width: 20
            - Fill:
                height: 10
            - HorizontalContainer:
                name: last_hori
                children:
                    - PushButton:
                        name: Do something
                        tooltip: Add some tool here
                        width: 100
                    - Slider:
                        name: Test slider
            - HorizontalContainer:
                children:
                    - Number:
                        name: Some number
                        value: 0.5
                    - Number:
                        name: Another number
                    - IntNumber:
                        name: Some int number
                        max: 100
            - Fill:
                height: 30
            - HorizontalContainer:
                children:
                    - Fill:
                        width: 20
                    - Image:
                        image: Mandril.png
                    - Label:
                        name: Foobar
                    - Label:
                        name: Barfoo
            - Fill:
                height: 15
            - HorizontalContainer:
                children:
                    - Label:
                        name: Foofoo
                    - Number:
                        name: Some number
                    - Fill:
                        width: 50
    '''

hotkeys = '''
d:
    press: d_was_pressed
    release: d_was_released
s: foobar
q: quit_script
'''

class Events():
    @staticmethod
    def d_was_pressed(elem):
        print 'you pressed d!'
    
    @staticmethod
    def d_was_released(elem):
        print 'you released d!'
    
    @staticmethod
    def foobar(elem):
        print 'foobar'
    
    @staticmethod
    def quit_script(elem):
        Draw.Exit()

# ----------------- INITIALIZATION -------------------
if __name__ == '__main__':
    app = BlenderApplication(UIStructure, hotkeys, Events)
    app.run()