#!/usr/bin/env python

import os
import sys
import numpy as np

from datetime import datetime, timedelta

from xarray_IO import xarray_IO
from spectral import spectral
from plot_tools import plot_tools

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

#        self.start_time = datetime(2020, 10, 9, 0)
        self.start_time = datetime.now()

        # +++ Initialize model grid +++ #
        pass

        # +++ Initialize spectral routines +++ #
        pass

        # +++ Initialize model fields +++ #
        pass

        # +++ Initialize forcing +++ #
        pass

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

        for it in range(self.nsteps):

            # +++ Dynamics +++ #
            pass

            ######

            # +++ Timestep +++ #
            pass

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

        for it in range(self, nsteps):

            # +++ Dynamics +++ #
            pass

            ######

            # +++ Timestep +++ #
            pass

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
    pass

#############################
### +++ END OF SCRIPT +++ ###
#############################
