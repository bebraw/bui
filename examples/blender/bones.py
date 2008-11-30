import bpy
from Blender import Draw, Scene, Types, Window

from bui.serializer import unserialize

from bui.blender.application import Application

class UIStructure():
    root_structure = '''
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
        height: 20
        width: 200
        event_handler: test_handler
    '''

hotkeys = '''
q: quit_script
'''

class Events():
    @staticmethod
    def quit_script(elem):
        Draw.Exit()
    
    @staticmethod
    def test_handler(elem):
        print 'now in test handler'
        print elem.value
        try:
            ob = bpy.data.objects[elem.name]
            ob.LocZ = elem.value
        except:
            pass

class Constraints():
    @staticmethod
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
                            new_bone = unserialize(UIStructure, UIStructure.slider_structure)
                            armature_bones_elem.add_child_structure(new_bone)
                            new_bone.name = bone_name
                
                # check if a bone has been removed
                armature_bones = root_elem.find_child(name='armature_bones')
                elems_to_remove = []
                
                for armature_bone in armature_bones.children:
                    found_bone = False
                    
                    for bone_name in p.bones.keys():
                        if armature_bone.name == bone_name:
                            found_bone = True
                            break
                    
                    if not found_bone:
                        elems_to_remove.append(armature_bone)
                
                for elem in elems_to_remove:
                    armature_bones.children.remove(elem)

if __name__ == '__main__':
    app = Application(UIStructure, hotkeys, Events, Constraints)
    app.run()
