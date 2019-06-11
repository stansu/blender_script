import bpy
import glob
import os

imd = '/home/stan/Downloads'
print(imd)
os.chdir(imd)

for files in glob.glob("*.fbx"):
    print( files )
    bpy.ops.import_scene.fbx(filepath=files)
