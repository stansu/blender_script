import bpy

class StanPanel(bpy.types.Panel):
    """Creates a Panel in the tool shelf"""
    bl_label = "Stan's Panel"
    bl_idname = "stan_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "STAN"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        circleOps = row.operator("mesh.primitive_circle_add", icon='MESH_CIRCLE')
        circleOps.vertices = 8
        circleOps.radius = 10
        circleOps.fill_type = 'NGON'
        circleOps.location = (0, 0, 0)
        
        row = layout.row()
        row.operator("object.editmode_toggle", icon='EDIT')
        
        row = layout.row()
        row.operator("view3d.edit_mesh_extrude_move_normal", icon='FACESEL')
        
        row = layout.row()
        row.operator("transform.resize", icon='MAN_SCALE')
        
        row = layout.row()
        moveOps = row.operator("transform.translate", icon='MAN_TRANS')
        moveOps.constraint_axis = (False, False, True)
        
        

def register():
    bpy.utils.register_class(StanPanel)

def unregister():
    bpy.utils.unregister_class(StanPanel)

if __name__ == "__main__":
    register()
