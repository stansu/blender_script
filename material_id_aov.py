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
            
    # check material have (id) node
    if not i.node_tree.nodes.get('AOV Output'):
        
        # if not, create id nodes
        stan_id = i.node_tree.nodes.new('ShaderNodeOutputAOV')
        stan_id.name = 'id'
        stan_id.inputs[0].default_value = [random.random() for i in range(4)]
        stan_id.inputs[0].default_value[3] = 1