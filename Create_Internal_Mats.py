# import modules
import bpy

# create a object contain all materials
mats = bpy.data.materials

# make sure all materials not use nodes
for i in mats:
    i.use_nodes = False

# start looping all materials
for i in mats:
    tex = bpy.data.textures.new("bake", 'IMAGE')
    slot = i.texture_slots.add()
    slot.texture = tex
    img = i.node_tree.nodes.get("Image Texture").image
    slot.texture.image = img
