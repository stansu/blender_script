import bpy, os

tempString = ''
tempArmature = bpy.data.armatures[0]
tempFile = tempArmature.name

for b in tempArmature.bones:
    tempString += b.name + '\n'

if bpy.data.texts.find(tempFile) == -1:
    bpy.data.texts.new(tempFile)
    bpy.data.texts[tempFile].from_string(tempString)
else:
    bpy.data.texts[tempFile].from_string(tempString)
    