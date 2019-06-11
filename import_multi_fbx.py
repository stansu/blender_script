import bpy
import glob
import os

imd = '/home/stan/Downloads'
os.chdir(imd)

for files in glob.glob("*.fbx"):
    bpy.ops.import_scene.fbx(filepath=files)
