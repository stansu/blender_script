# import modules
import bpy, random

# create a object contain all materials
mats = bpy.data.materials

# make sure all materials use nodes
for i in mats:
    if not i.use_nodes:
        i.use_nodes = True

# start looping all materials
for i in mats:
    
    # check material have (Material Output) node
    if i.node_tree.nodes.get('Material Output'):
        
        # create original linkin objects
        old_BSDF_out = i.node_tree.nodes['Material Output'].inputs[0].links[0].from_socket
        surf_in = i.node_tree.nodes['Material Output'].inputs[0]
        
        # check material have (stan_mix) node
        if not i.node_tree.nodes.get('stan_mix'):
            
            # if not, create stan_* nodes
            stan_mix = i.node_tree.nodes.new('ShaderNodeMixShader')
            stan_mix.name = 'stan_mix'
            stan_mix.inputs[0].default_value = 0
            stan_mix_in_s1 = stan_mix.inputs[1]
            stan_mix_in_s2 = stan_mix.inputs[2]
            stan_mix_out_s = stan_mix.outputs[0]
            stan_emit = i.node_tree.nodes.new('ShaderNodeEmission')
            stan_emit.name = 'stan_emit'
            temp_color = [random.random() for i in range(4)]
            temp_color[3] = 1
            stan_emit.inputs[0].default_value = temp_color
            stan_emit_out = stan_emit.outputs[0]
            
            # create new links
            i.node_tree.links.new(stan_emit_out, stan_mix_in_s2)
            i.node_tree.links.new(old_BSDF_out, stan_mix_in_s1)
            i.node_tree.links.new(stan_mix_out_s, surf_in)
        else:
            stan_mix = i.node_tree.nodes['stan_mix']
        
        # toggle emit materials
        if stan_mix.inputs[0].default_value == 0:
            stan_mix.inputs[0].default_value = 1
        else:
            stan_mix.inputs[0].default_value = 0
