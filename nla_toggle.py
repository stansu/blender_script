import bpy

for i in bpy.data.objects:
    if i.animation_data is not None:
        for j in i.animation_data.nla_tracks:
            for k in j.strips:
                if k.select:
                    k.use_reverse = not k.use_reverse

