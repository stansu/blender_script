import bpy, os

tempString = ''

for a in bpy.data.armatures:
    for b in a.bones:
        tempString += a.name + ',' + b.name + '\n'

tempFile = os.path.splitext(bpy.path.basename(bpy.data.filepath))[0]

if bpy.data.texts.find(tempFile) == -1:
    bpy.data.texts.new(tempFile)
    bpy.data.texts[tempFile].from_string(tempString)
else:
    bpy.data.texts[tempFile].from_string(tempString)
    
