import bpy

win      = bpy.context.window
scr      = win.screen
areas3d  = [area for area in scr.areas if area.type == 'VIEW_3D']
region   = [region for region in areas3d[0].regions if region.type == 'WINDOW']

override = {'window':win,
            'screen':scr,
            'area'  :areas3d[0],
            'region':region,
            'scene' :bpy.context.scene,
            }
            
bpy.ops.view3d.snap_cursor_to_selected(override)