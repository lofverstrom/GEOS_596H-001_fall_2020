#!/usr/bin/env python

"""
Namelist for barotropic model
"""

import os

#############################

# Time stepping
nsteps = 100        # Number of time steps to integrate
dt = 10.*60.         # Timestep (seconds)


# Spectral operators
trunc = None        # Truncation (if None, defaults to # latitudes)
rsphere = 6.3712e6  # Planetary radius
legfunc = 'stored'  # Legendre functions


# I/O
output_dir = os.path.join(os.getcwd(), 'output')  # Output directory
output_freq = 6     # Freq. of output in hours (0 = no data saved)

plot_dir = os.path.join(os.getcwd(), 'figures')   # Figure directory
plot_freq = 6       # Freq. of output figures in hours (0 = no plots)
