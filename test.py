import bpy

def enum_members_from_type(rna_type, prop_str):
    prop = rna_type.bl_rna.properties[prop_str]
    return [e.identifier for e in prop.enum_items]

def enum_members_from_instance(rna_item, prop_str):
    return enum_members_from_type(type(rna_item), prop_str)

class SculptOperator(bpy.types.Operator):
    bl_idname = "sculpt.dialog_operator"
    bl_label = "sculpt Dialog Operator"

    my_EnumProperty = bpy.props.EnumProperty(
        items = ['SUBDIVIDE', 'COLLAPSE', 'SUBDIVIDE_COLLAPSE'])

    def execute(self, context):
        bpy.context.scene.tool_settings.sculpt.detail_refine_method = self.my_EnumProperty
        return {'FINISHED'}

    def check(self, context):
        return True

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "my_EnumProperty")


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

bpy.utils.register_class(SculptOperator)

# test call
bpy.ops.object.dialog_operator('INVOKE_DEFAULT')