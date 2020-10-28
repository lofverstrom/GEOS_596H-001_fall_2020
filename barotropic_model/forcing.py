#!/usr/bin/env python

import numpy as np
from xarray_IO import xarray_IO
import namelist as nl

#############################

class forcing:
    def __init__(self, latr, lonr):

        self.dtype = nl.dtype

        self.latr = latr
        self.lonr = lonr

        self.lonsr, self.latsr = np.meshgrid(lonr, latr)

        self.latd = np.rad2deg(latr)
        self.lond = np.rad2deg(lonr)

        self.ny = len(self.latr)
        self.nx = len(self.lonr)

        ##

        # Topography forcing
        self.topo = np.zeros((self.ny, self.nx), dtype=self.dtype)
        self.topo_clatr = np.deg2rad(nl.topo_clatd)
        self.topo_clonr = np.deg2rad(nl.topo_clond)
        self.topo_height = nl.topo_height


        ###

    def topography_gaussian(self):

        self.topo = np.cos(self.rlats) * \
            np.exp(-(self.lonsr-self.topo_clonr)**2/.1) * \
            np.exp(-(self.latsr-self.topo_clatr)**2/.3)

        self.topo = self.topo_height * (self.topo / np.amax(self.topo))

        return self.topo
        
        
#############################
if __name__ == '__main__':
    pass

#############################
# # +++ END OF SCRIPT +++ # #
#############################
