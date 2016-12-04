bl_info = {
    "name": "Interface Translation Toggle",
    "author": "stan",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "",
    "description": "Toggle interface's translation",
    "warning": "",
    "wiki_url": "stan.stz@gmail.com",
    "category": "User Interface"}

import bpy

class Translation(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.translation"
    bl_label = "Interface translation"

    def execute(self, context):
        use_translate = bpy.context.user_preferences.system.use_translate_interface
        bpy.context.user_preferences.system.use_translate_interface = not use_translate
        return {'FINISHED'}

def addon_button(self, context):
     self.layout.operator(
          "object.translation",
          text="Translation",)


def register():
    bpy.utils.register_class(Translation)
    bpy.types.INFO_HT_header.append(addon_button)

def unregister():
    bpy.utils.unregister_class(Translation)
    bpy.types.INFO_HT_header.remove(addon_button)

if __name__ == "__main__":
    register()
