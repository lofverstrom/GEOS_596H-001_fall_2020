#!/usr/bin/env python

"""
Namelist for barotropic model
"""

import os
import numpy as np

#############################

# Time stepping
nsteps = 100        # Number of time steps to integrate
dt = 10.*60.        # Timestep (seconds)
nforward = 20       # Forward step every # timesteps


# Spectral operators
trunc = None        # Truncation (if None, defaults to # latitudes)
rsphere = 6.3712e6  # Planetary radius
legfunc = 'stored'  # Legendre functions


# I/O
output_dir = os.path.join(os.getcwd(), 'output')  # Output directory
output_freq = 6     # Freq. of output in hours (0 = no data saved)

plot_dir = os.path.join(os.getcwd(), 'figures')   # Figure directory
plot_freq = 6       # Freq. of output figures in hours (0 = no plots)


# Idealized topographic forcing
topo_clatd = 45.     # center latitude (degrees)
topo_clond = 40.     # center longitude (degrees)
topo_height = 2500.  # topographic height (m)


# Misc
dtype = np.float32  # Precission
