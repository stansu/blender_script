import bpy

objs = bpy.context.selected_objects
links = ['OBJECT','DATA']

for o in objs:
  layers = o.data.uv_layers
  slots = o.material_slots
  if len(layers) > 0:
    layers[0].name = 'uv'
  if len(slots) > 0:
    slots[0].link = links[1]
