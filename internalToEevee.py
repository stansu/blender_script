import bpy

mats = bpy.data.materials

for m in mats:
    m.use_nodes = True
    mTree = m.node_tree
    mNodes = mTree.nodes
    if not mNodes.get('Material Output'):
        matOutput = mNodes.new("ShaderNodeOutputMaterial")
        emitMat = mNodes.new("ShaderNodeEmission")
        emitMat.inputs[0].default_value=m.diffuse_color
        mTree.links.new(emitMat.outputs[0], matOutput.inputs[0])
