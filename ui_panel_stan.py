import bpy

class StanPanel(bpy.types.Panel):
    '''Creates a Panel in the tool shelf'''
    bl_label = 'Stan Panel'
    bl_idname = 'stan_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'STAN'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        circleOps = row.operator('mesh.primitive_circle_add', icon='MESH_CIRCLE')
        circleOps.vertices = 8
        circleOps.radius = 10
        circleOps.fill_type = 'NGON'
        circleOps.location = (0, 0, 0)
        
        row = layout.row()
        row.operator('view3d.view_selected', icon='VIEWZOOM')
        
        row = layout.row()
        row.operator('object.editmode_toggle', icon='EDIT')
        
        row = layout.row()
        row.operator('mesh.select_mode', icon='EDGESEL', text="Edge").type = 'EDGE'
        
        row = layout.row()
        row.operator('ed.undo', icon='BACK')
        
        row = layout.row()
        row.operator('view3d.edit_mesh_extrude_move_normal', icon='FACESEL')
        
        row = layout.row()
        row.operator('transform.resize', icon='MAN_SCALE')
        
        row = layout.row()
        moveOps = row.operator('transform.translate', icon='MAN_TRANS')
        moveOps.constraint_axis = (False, False, True)
        
        row = layout.row()
        row.operator('mesh.select_all', icon='RESTRICT_SELECT_OFF')
        
        row = layout.row()
        shadeOps = row.operator('wm.context_toggle_enum', icon='SOLID', text='Solid')
        shadeOps.data_path = 'space_data.viewport_shade'
        shadeOps.value_1 = 'SOLID'
        shadeOps.value_2 = 'WIREFRAME'
        
        row = layout.row()
        row.operator('view3d.select_border', icon='BORDER_RECT')
        
        row = layout.row()
        row.operator('view3d.view_persportho', icon='VIEW3D')
        
        row = layout.row()
        frontOps = row.operator('view3d.viewnumpad', icon='AXIS_FRONT', text='Front')
        frontOps.type = 'FRONT'
        
        row = layout.row()
        sdOps = row.operator('object.subdivision_set', icon='MOD_SUBSURF')
        sdOps.level = 2
        
        row = layout.row()
        row.operator('object.delete', icon='CANCEL')

def register():
    bpy.utils.register_class(StanPanel)

def unregister():
    bpy.utils.unregister_class(StanPanel)

if __name__ == '__main__':
    register()
