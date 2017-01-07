import bpy
import subprocess

class TextToVoice(bpy.types.Operator):
    bl_idname = "voice.speak"
    bl_label = "Speak"
    text = bpy.props.StringProperty()
    text = "Type text to speak"
 
    def execute(self, context):
        path='C:\Program Files (x86)\eSpeak\command_line\espeak.exe'
        subprocess.run([path, '-s120', self.text])
        return{'FINISHED'}  



def addon_button(self, context):
    self.layout.operator(
          "voice.speak",
          text="Speak",)
    ###self.layout.prop(bpy.ops.voice.speak,['text'])

def register():
    bpy.utils.register_class(TextToVoice)
    bpy.types.INFO_HT_header.append(addon_button)

def unregister():
    bpy.utils.unregister_class(TextToVoice)
    bpy.types.INFO_HT_header.remove(addon_button)

if __name__ == "__main__":
    register()