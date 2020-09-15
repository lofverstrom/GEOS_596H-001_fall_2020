#!/usr/bin/env python

import xarray as xr

#############################

class xarray_IO:
    """
    Basic xarray interface for netcdf I/O
    """
    def __init__(self, dfile=None, engine='netcdf4', FV=1.e20):
        pass

    def copy_variable(self):
        pass

    def create_dimension(self):
        pass

    def create_variable(self):
        pass

    def add_attributes(self):
        pass

    def write_netcdf(self):
        pass
        
        
#############################
        
if __name__ == "__main__":

    import numpy as np
    
#    dfile = '../data/ERAInt.surf_geopot.0.75x0.75.nc'
    dfile = '../data/ERAInt.t2m.ltm.0.75x0.75.nc'    
    
