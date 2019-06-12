import bpy
import os

basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")

scene = bpy.context.scene

bpy.ops.object.select_all(action='DESELECT')

for o in bpy.data.objects:
    if not o.data:
        scene.objects.active = o
        name = bpy.path.clean_name(o.name)
        fn = os.path.join(basedir, name)
        bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE')
        o.select = True
        bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)
        bpy.ops.object.select_all(action='DESELECT')
