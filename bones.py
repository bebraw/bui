from Blender import Draw, Scene, Types, Window

from bui.blender.application import BlenderApplication

# -------------------- UI STRUCTURE ----------------
ui_structure = '''
VerticalContainer:
    width: 400
    children:
        - HorizontalContainer:
            name: test_hori
            children:
                - Label:
                    name: Great bone script v0.1
                - PushButton:
                    name: X
                    tooltip: Quit script
                    event_handler: quit_script
                    width: 20
        - VerticalContainer:
            name: armature_bones
'''

slider_structure = '''
Slider:
    min: 0.0
    max: 1.0
    value: 0.5
'''

# ------------------------ HOTKEYS ---------------------
hotkeys = '''
q: quit_script
'''

# ------------------------ EVENT HANDLERS --------------
def quit_script(elem):
    Draw.Exit()

# ----------------- CONSTRAINTS ----------------------
def check_bones_constraint(root_elem):
    scene = Scene.GetCurrent() 
    active = scene.objects.active     
    active_data = active.getData() 
    
    if type(active_data) == Types.ArmatureType: 
        if Window.PoseMode() == True: 
            armature_object = active 
            armature_data = armature_object.getData() 
            p = armature_object.getPose() 
            
            for bone_name in p.bones.keys(): 
                if bone_name[:3] == "SLI":
                    bone_elem = root_elem.find_child(name=bone_name)
                    
                    if not bone_elem:
                        armature_bones_elem = root_elem.find_child(name='armature_bones')
                        new_elem = armature_bones_elem.add_child_structure(slider_structure, globals())
                        new_elem.name = bone_name
                        return new_elem # TODO: remember to get rid of this mechanism... this won't work (returns only first bone found!). this needs to be rethought

# ----------------- INITIALIZATION -------------------
if __name__ == '__main__':
    app = BlenderApplication(ui_structure, hotkeys, globals())
    app.run()
