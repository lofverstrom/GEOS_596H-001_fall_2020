#!/usr/bin/env python

from spectral import spectral
from xarray_IO import xarray_IO
from plot_tools import plot_tools
import numpy as np

import sys

############################

if __name__ == "__main__":

    dpath = "./input_data"

    ufile = '{}/u.ltm.T42.bilinear.nc'.format(dpath)
    vfile = '{}/v.ltm.T42.bilinear.nc'.format(dpath)

    dsu = xarray_IO(ufile)
    dsv = xarray_IO(vfile)

    lat = dsu.get_values('lat')
    lon = dsu.get_values('lon')

    u = dsu.get_values('u')
    v = dsv.get_values('v')

    lat = lat[::-1]
    u = u[::-1, :]
    v = v[::-1, :]

    ###

    pp = plot_tools(central_longitude=270.)

    # Stat by plotting u
    pp.quick_plot(lat, lon, u, add_cyclic=True)

    ###

    # Initialize spectral
#    spec = spectral(lat, lon)

    ##

    # Caluclate horizontal gradients
#    dudx, dudy = spec.gradient(u)
#    pp.quick_plot(lat, lon, dudy, add_cyclic=True)

    ##

    # Calculate planetart and relative vorticity
#    vrt = spec.uv2vrt(u, v)
#    f = spec.planetaryvorticity()

#    pp.quick_plot(lat, lon, vrt, add_cyclic=True)

    ##

    # Calculate geostrophic streamfunction and velocity potential
#    psi, chi = spec.uv2sfvp(u, v)

    # Remove zonal mean
#    psi -= psi.mean(axis=-1)[:, None]

#    pp.quick_plot(lat, lon, psi, add_cyclic=True)

    ##

    # Assess error from spectral transform
#    vrt, div = spec.uv2vrtdiv(u, v)
#    u0, v0 = spec.vrtdiv2uv(vrt, div)

#    levels = np.linspace(-1.e-2, 1.e-2, 21)
#    pp.quick_plot(lat, lon, u-u0, add_cyclic=True, levels=levels)


#############################
### +++ END OF SCRIPT +++ ###
#############################
