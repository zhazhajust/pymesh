import pymesh
import numpy as np
import matplotlib.pyplot as plt

##########################################
############ Rotate Mesh Data ############
##########################################

wkdir = "../../Render/"

ey = np.load(wkdir + "/Ez.npy")[::2, ::50]

m, n = ey.shape[0], ey.shape[1]
res = np.zeros([m, n, n])
pymesh.rotate(ey, res, ifhalf = False)

fig = plt.figure(figsize=(4, 3))
plt.contourf(res[:, int(n/2), :].T)
cbar = plt.colorbar()

##########################################
############# Save Mesh Data #############
##########################################

mesh = pymesh.get_iso_surf(res, contours_number = 4, cmap = "jet")
color = pymesh.interp_color(mesh.iso_vals, pltmap = "jet")
mesh.export(wkdir + "test", "obj")
