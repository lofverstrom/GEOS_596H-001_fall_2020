#!/usr/bin/env python

import os
import sys
import numpy as np

from datetime import datetime, timedelta

from xarray_IO import xarray_IO
from spectral import spectral
from plot_tools import plot_tools
from forcing import forcing
import namelist as nl

#############################


class barotropic:
    """
    Barotropic vorticity model
    """

    def __init__(self):

        # +++ Initialize time stepping +++ #
        self.nsteps = nl.nsteps
        self.dt = nl.dt

        self.nforward = nl.nforward  # forward step every # steps

#        self.start_time = datetime(2020, 10, 9, 0)
        self.start_time = datetime.now()

        # +++ Initialize model grid +++ #
        self.latd = np.linspace(90., -90., 64)  # dummy arguments
        self.lond = np.linspace(0., 360., 128)  # dummy arguments

        self.latr = np.deg2rad(self.latd)
        self.lonr = np.deg2rad(self.lond)

        self.ny = len(self.latd)
        self.nx = len(self.lond)

        # +++ Initialize spectral routines +++ #
        self.s = spectral(self.latd, self.lond)

        # +++ Initialize model fields +++ #
        self.vortp_tend = np.zeros((self.ny, self.nx))

        self.vortp = np.zeros((self.ny, self.nx, 3))

        # +++ Initialize forcing +++ #
        self.f = forcing(self.latr, self.lonr)
        self.topo = self.f.topography_simple()
        self.dxtopo, self.dytopo = self.s.gradient(self.topo)


#        pp = plot_tools()
#        pp.quick_plot(self.latd, self.lond, self.topo)
#        pp.quick_plot(self.latd, self.lond, self.dxtopo)

        # +++ Model diagnostics +++ #
        # netCDF output
        self.output_freq = nl.output_freq
        self.output_dir = nl.output_dir
        # Create directory if not existing
        if not os.path.isdir(self.output_dir):
            os.mkdir(self.output_dir)

        # Plot figures
        self.plot_freq = nl.plot_freq
        self.plot_dir = nl.plot_dir
        # Create directory if not existing
        if not os.path.isdir(self.plot_dir):
            os.mkdir(self.plot_dir)


#############################


    def integrate_linear_dynamics(self):
        """
        Linear dynamics
        """

        # Initialize loop indices
        im = 2
        ic = 0
        ip = 1

        for it in range(self.nsteps):

            # +++ Reset tendencies +++ #
            self.vortp_tend *= 0.

            # +++ Dynamics +++ #
            pass

            ######

            # +++ Timestep +++ #
            if it % self.nforward == 0:
                # Forward step
                self.vortp[:, :, ip] = self.vortp[:, :, ic] - self.dt*self.vortp_tend
            else:
                # Leapfrog step
                self.vortp[:, :, ip] = self.vortp[:, :, im] - 2.*self.dt*self.vortp_tend

            # update time-pointers (cyclic permutation)
            itmp = im
            im = ic
            ic = ip
            ip = itmp

            ######

            # +++ Diagnostics +++ #

            # Current hour and integration time
            chr = (it+1) * self.dt / 3600.
            itime = self.start_time + timedelta(hours=chr)

            # Plot figures
            if self.plot_freq != 0 and chr % self.plot_freq == 0:
                print('-- Step {}: plotting fields'.format(it))

            ###

            # Save output data
            if self.output_freq != 0 and chr % self.output_freq == 0:
                print('-- Step {}: saving data'.format(it))


#############################


    def integrate_nonlinear_dynamics(self):
        """
        Nonlinear dynamics
        """

        # Initialize loop indices
        im = 2
        ic = 0
        ip = 1

        for it in range(self.nsteps):

            # +++ Reset tendencies +++ #
            self.vortp_tend *= 0.

            # +++ Dynamics +++ #
            pass

            ######

            # +++ Timestep +++ #
            if it % self.nforward == 0:
                # Forward step
                self.vortp[:, :, ip] = self.vortp[:, :, ic] - self.dt*self.vortp_tend
            else:
                # Leapfrog step
                self.vortp[:, :, ip] = self.vortp[:, :, im] - 2.*self.dt*self.vortp_tend

            # update time-pointers (cyclic permutation)
            itmp = im
            im = ic
            ic = ip
            ip = itmp

            ######

            # +++ Diagnostics +++ #

            # Current hour and integration time
            chr = (it+1) * self.dt / 3600.
            itime = self.start_time + timedelta(hours=chr)

            # Plot figures
            if self.plot_freq != 0 and chr % self.plot_freq == 0:
                print('-- Step {}: plotting fields'.format(it))

            ###

            # Save output data
            if self.output_freq != 0 and chr % self.output_freq == 0:
                print('-- Step {}: saving data'.format(it))

            ###

#############################


if __name__ == '__main__':

    #    model = barotropic()
    #    model.integrate_linear_dynamics()

    pass

#############################
### +++ END OF SCRIPT +++ ###
#############################
