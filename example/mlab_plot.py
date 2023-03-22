import pymesh
from mayavi import mlab

##########################################
############# Load Mesh Data #############
##########################################

wkdir = "/Users/mac/Documents/VScode/python/Render/"
mesh = pymesh.Mesh.load(wkdir + "test", "obj")

##########################################
############# Plot Mesh Data #############
##########################################

mesh.verts[:, 0] *= 1/10
mlab_mesh = pymesh.iso_surface(mesh, colormap = "RdBu")
mlab.colorbar()
mlab.show()