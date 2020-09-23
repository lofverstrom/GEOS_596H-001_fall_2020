#!/usr/bin/env python

import xarray as xr

#############################


class xarray_IO:
    """
    Basic xarray interface for netcdf I/O
    """

    def __init__(self, dfile=None, engine='netcdf4', FV=1.e20):
        if dfile is not None:
            self.ds = xr.open_dataset(dfile)
        else:
            self.ds = xr.Dataset()

        self.engine = engine
        self._FV = FV

    ###

    def copy_variable(self, dsin, field):
        self.ds[field] = dsin[field]

    ###

    def create_dimension(self, var, field, **attributes):
        self.ds[field] = xr.DataArray(var, coords=[(field, var)])

        try:
            self.ds[field].encoding['_FillValue'] = self._FV
        except Exception:
            pass

        try:
            self.add_attributes(var, field, **attributes)
        except Exception:
            pass

    ###

    def create_variable(self, var, field, dims, **attributes):
        """
        Variable dims is given as a tuple, e.g., ('time', 'lat', 'lon')
        """
        self.ds[field] = xr.DataArray(var, dims=dims)

        try:
            self.ds[field].encoding['_FillValue'] = self._FV
        except Exception:
            pass

        try:
            self.add_attributes(var, field, **attributes)
        except Exception:
            pass

    ###

    def add_attributes(self, var, field, **attributes):
        try:
            for attr, value in attributes.items():
                self.ds[field].attrs[attr] = value
        except Exception:
            print('-- ERROR: Variable {} is not defined'.format(field))

    ###

    def write_netcdf(self, dfile, engine='netcdf4'):
        self.ds.to_netcdf(path=dfile, mode='w', engine=engine)


#############################

if __name__ == "__main__":

    pass
