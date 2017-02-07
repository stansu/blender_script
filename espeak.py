import bpy
import subprocess

class TextToVoice(bpy.types.Operator):
    bl_idname = "object.speak"
    bl_label = "Speak"
    
#    text = bpy.props.StringProperty()
#    text = "Type text to speak"
 
    def execute(self, context):
#        path='C:\Program Files (x86)\eSpeak\command_line\espeak.exe'
#        subprocess.run([path, '-s120', self.text])
        return{'FINISHED'}

class SpeakMakePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
#    bl_context = "objectmode"
    bl_category = "stan"
    bl_label = "Speak"
        
    def draw(self, context):
#        TheCol = self.layout.column(align=True)
        TheCol = self.layout
        TheCol.prop(context.scene, "speak_string")
        TheCol.operator("object.speak", text="Speak")
#        TheCol.props(self.text)


def addon_button(self, context):
    self.layout.operator(
          "object.speak",
          text="Speak",)
    self.layout.prop(context.scene, "speak_string")

def register():
    bpy.utils.register_class(TextToVoice)
#    bpy.utils.register_class(SpeakMakePanel)
    bpy.types.Scene.speak_string = bpy.props.StringProperty \
      (
        name = "text_to_speak",
        description = "type text here to speak",
        default = "Type text to speak"
      )
    bpy.types.INFO_HT_header.append(addon_button)

def unregister():
    bpy.utils.unregister_class(TextToVoice)
#    bpy.utils.unregister_class(SpeakMakePanel)
    bpy.types.INFO_HT_header.remove(addon_button)
    del bpy.types.Scene.speak_string

if __name__ == "__main__":
    register()