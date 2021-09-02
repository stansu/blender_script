import bpy, random

for m in bpy.data.materials:
    m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1),1)