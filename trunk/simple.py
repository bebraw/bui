from Blender import Draw

from bui.blender.application import BlenderApplication

# -------------------- UI STRUCTURE ----------------
ui_structure = '''
VerticalContainer:
    width: 400
    children:
        - HorizontalContainer:
            children:
                - Label:
                    name: Test script
                - PushButton:
                    name: X
                    tooltip: Quit script
                    event_handler: quit_script
                    width: 20
        - EmptyContainer:
            height: 10
        - HorizontalContainer:
            children:
                - PushButton:
                    name: Do something
                    tooltip: Add some tool here
                    width: 100
'''

# ------------------------ HOTKEYS ---------------------
hotkeys = '''
q: quit_script
'''

# ------------------------ EVENT HANDLERS --------------
def quit_script(elem=None):
    Draw.Exit()

# ----------------- INITIALIZATION -------------------
if __name__ == '__main__':
    app = BlenderApplication(ui_structure, hotkeys, globals())
    app.run()