import bpy

for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.show_manipulator = True
                if space.transform_manipulators == {'TRANSLATE'}:
                    space.transform_manipulators = {'ROTATE'}
                elif space.transform_manipulators == {'ROTATE'}:
                    space.transform_manipulators = {'SCALE'}
                elif space.transform_manipulators == {'SCALE'}:
                    space.transform_manipulators = {'TRANSLATE'}