import bpy

for m in bpy.data.materials:
    m.use_backface_culling = True
    try:
        m.node_tree.nodes['Principled BSDF'].input[4].default_value = 0
        m.node_tree.nodes['Principled BSDF'].input[5].default_value = 0
    except:
        pass