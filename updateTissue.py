import bpy

tempActive = bpy.context.active_object
tempFirst = True

for o in bpy.data.objects:
    if o.tissue_tessellate.generator != '':
        if tempFirst:
            bpy.context.scene.objects.active = o
            bpy.ops.object.update_tessellate()
            bpy.ops.object.update_tessellate()
            tempFirst = False
        else:
            bpy.context.scene.objects.active = o
            bpy.ops.object.update_tessellate()

bpy.context.scene.objects.active = tempActive