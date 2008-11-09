from Blender import Draw

from bui.blender.application import BlenderApplication

# -------------------- UI STRUCTURE ----------------
ui_structure = '''
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
        - EmptyContainer:
            name: empty_cont
            height: 10
        - HorizontalContainer:
            name: last_hori
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
