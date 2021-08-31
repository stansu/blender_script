import bpy, os

tempString = ''
tempFile = os.path.splitext(bpy.path.basename(bpy.data.filepath))[0]
bpy.data.texts.new(tempFile)
for a in bpy.data.armatures:
    for b in a.bones:
        tempString += a.name + ',' + b.name + '\n'

bpy.data.texts[tempFile].from_string(tempString)