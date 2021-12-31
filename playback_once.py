import bpy, time

s = bpy.context.scene
fStart = s.frame_start
fEnd = s.frame_end
fps = s.render.fps

for f in range(fStart, fEnd+1):
    time.sleep(1/fps)
    s.frame_current = f
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)