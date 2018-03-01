import bpy

for obj in bpy.context.selected_objects:
    if obj.animation_data is not None:
        action = obj.animation_data.action
        if action is not None:
            track = obj.animation_data.nla_tracks.new()
            track.strips.new(action.name, action.frame_range[0], action)
            obj.animation_data.action = None
