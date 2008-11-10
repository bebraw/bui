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

# TODO: it should be possible to write this ~without~ container structure!
slider_structure = '''
VerticalContainer:
    children:
        - Slider:
            name: slider
            min: 0.0
            max: 1.0
            value: 0.5
'''

# ------------------------ HOTKEYS ---------------------
# TODO: hotkey mapping does not work yet!
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
            
            # check if a bone has to be added
            for bone_name in p.bones.keys(): 
                if bone_name[:3] == "SLI":
                    bone_elem = root_elem.find_child(name=bone_name)
                    
                    if not bone_elem:
                        armature_bones_elem = root_elem.find_child(name='armature_bones')
                        new_elem = armature_bones_elem.add_child_structure(slider_structure, globals())
                        new_bone = new_elem.find_child(name='slider')
                        new_bone.name = bone_name
            
            # check if a bone has been removed
            bone_elems = root_elem.find_child('armature_bones')
            elems_to_remove = []
            
            for elem in bone_elems.children:
                found_bone = False
                
                for bone_name in p.bones.keys():
                    if elem.children[0].name == bone_name:
                        found_bone = True
                        break
                
                if not found_bone:
                    elems_to_remove.append(elem)
            
            for elem in elems_to_remove:
                bone_elems.children.remove(elem)
                

# ----------------- INITIALIZATION -------------------
if __name__ == '__main__':
    app = BlenderApplication(ui_structure, hotkeys, globals())
    app.run()