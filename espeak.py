bl_info = {
    "name": "Speak English",
    "author": "stan",
    "version": (1, 0),
    "blender": (2, 78, 0),
    "description": "Speak English",
    "category": "User Interface"}

import bpy
import subprocess

class TextToVoice(bpy.types.Operator):
    bl_idname = "object.speak"
    bl_label = "Speak"
    
    def execute(self, context):
        path='/usr/bin/espeak'
        subprocess.run([path, '-s120', bpy.context.scene.speak_string])
        return{'FINISHED'}

def addon_button(self, context):
    self.layout.operator(
          "object.speak",
          text="Speak",)
    self.layout.prop(context.scene, "speak_string")

def register():
    bpy.utils.register_class(TextToVoice)
    bpy.types.Scene.speak_string = bpy.props.StringProperty \
      (
        name = "",
        description = "type text here to speak",
        default = "Type text to speak"
      )
    bpy.types.INFO_HT_header.append(addon_button)

def unregister():
    bpy.utils.unregister_class(TextToVoice)
    bpy.types.INFO_HT_header.remove(addon_button)
    del bpy.types.Scene.speak_string

if __name__ == "__main__":
    register()