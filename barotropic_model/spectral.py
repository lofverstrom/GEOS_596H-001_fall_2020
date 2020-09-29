#!/usr/bin/env python

import sys

import numpy as np
from spharm import Spharmt #, getspecindx, gaussian_lats_wts
#import time

#############################


class spectral:
    def __init__(self, lat, lon, 
                 rsphere=6.3712e6, legfunc='stored'):

        # Length of lat/lon arrays
        self.nlat = len(lat)
        self.nlon = len(lon)

        if self.nlat % 2:
            gridtype = 'gaussian'
        else:
            gridtype = 'regular'

        self.s = Spharmt(self.nlon, self.nlat, gridtype=gridtype,
                         rsphere=rsphere, legfunc=legfunc)

        # Reverse latitude array if necessary
#        self.ReverseLat = False
#        if lat[0] < lat[-1]:
#            lat = self._reverse_lat(lat)
#            self.ReverseLat = True

        # lat/lon in degrees
        self.glat = lat
        self.glon = lon

        # lat/lon in radians
        self.rlat = np.deg2rad(lat)
        self.rlon = np.deg2rad(lon)

        self.rlons, self.rlats = np.meshgrid(self.rlon, self.rlat)

        # Constants
        # Earth's angular velocity
        self.omega = 7.292e-05  # unit: s-1
        # Gravitational acceleration
        self.g = 9.8  # unit: m2/s

        # Misc
        self.dtype = np.float32

    def _reverse_lat(self, var):
        if len(np.shape(var)) == 1:
            return(var[::-1])
        if len(np.shape(var)) == 2:
            return(var[::-1, :])
        if len(np.shape(var)) == 3:
            return(var[:, ::-1, :])

    def planetaryvorticity(self, omega=None):
        pass
        

    def uv2vrt(self, u, v, trunc=None):
        """
        Calculate relative vorticity from horizonal wind field
        Input:  u and v  (grid)
        Output: relative vorticity (grid)
        """
        
        vrts, _ = self.s.getvrtdivspec(u, v, ntrunc=trunc)
        vrtg = self.s.spectogrd(vrts)
        return(vrtg)

    def uv2div(self, u, v, trunc=None):
        pass

    def uv2sfvp(self, u, v, trunc=None):
        """
        Calculate geostrophic streamfuncion and 
        velocity potential from u and v winds
        """
        
        psig, chig = self.s.getpsichi(u, v, ntrunc=trunc)
        return(psig, chig)

    
    def uv2vrtdiv(self, u, v, trunc=None):
        """
        Calculate relative vorticity and divergence
        from u and v winds
        """
        
        vrts, divs = self.s.getvrtdivspec(u, v, ntrunc=trunc)
        vrtg = self.s.spectogrd(vrts)
        divg = self.s.spectogrd(divs)
        return(vrtg, divg)

    
    def vrtdiv2uv(self, vrt, div, realm='grid', trunc=None):
        """
        # Get u,v from vrt, div fields
        # Input either in grid space
        # or in spectral space
        """
        if realm in ['g', 'grid']:
            vrts = self.s.grdtospec(vrt, trunc)
            divs = self.s.grdtospec(div, trunc)
        elif realm in ['s', 'spec', 'spectral']:
            vrts = vrt
            divs = div
        ug, vg = self.s.getuv(vrts, divs)
        return(ug, vg)

    
    def gradient(self, var, trunc=None):
        """
        Calculate horizontal gradients
        """
        
        # if self.ReverseLat is True:
        #    var = self._reverse_lat(var)

        try:
            var = var.filled(fill_value=np.nan)
        except AttributeError:
            pass
        if np.isnan(var).any():
            raise ValueError('var cannot contain missing values')
        try:
            varspec = self.s.grdtospec(var, ntrunc=trunc)
        except ValueError:
            raise ValueError('input field is not compatitble')
        dxvarg, dyvarg = self.s.getgrad(varspec)
        return(dxvarg, dyvarg)


#############################

if __name__ == "__main__":
    pass
