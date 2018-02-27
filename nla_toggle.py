import bpy

for i in bpy.context.selected_objects:
    for j in i.animation_data.nla_tracks.values():
        for k in j.strips.values():
            if k.select:
                k.use_reverse = True
