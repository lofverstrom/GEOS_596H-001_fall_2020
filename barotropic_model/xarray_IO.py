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

    def get_values(self, field):
        return(self.ds[field].values)

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

    import numpy as np

#    dfile = '../data/ERAInt.surf_geopot.0.75x0.75.nc'
    dfile = '../data/ERAInt.t2m.ltm.0.75x0.75.nc'

    dsin = xarray_IO(dfile)
#    dsout = xarray_IO()

#################################
# == Copy variable from file == #

#    dsout.copy_variable(dsin.ds, 't2m')

#    dsout.create_variable(dsout.ds.t2m-273.15, 't2m_degC',
#                          ('time', 'latitude', 'longitude'),
#                          units='degC')

################
# Create custom variable

    """
    nx = len(dsin.ds['longitude'])
    ny = len(dsin.ds['latitude'])

    lat = np.linspace(-90.,90.,ny)
    lon = np.linspace(0.,360.,nx)

    y = np.linspace(-2.*np.pi,2*np.pi,ny)
    x = np.linspace(-2.*np.pi,2*np.pi,nx)
    X,Y = np.meshgrid(x,y)

    Z = np.sin(np.sqrt(X**2 + Y**2))

#    dsout.create_dimension(lat, 'lat',
#                           units='degrees_north',
#                           long_name='latitude')

    dsout.create_dimension(lon, 'lon',
                           units='degrees_east',
                           long_name='longitude')

    dsout.create_variable(Z, 'Z', dims=('lat','lon'),
                           units='m',
                           long_name='wave perturbation')
    """

#    dsout.create_variable(lat, 'lat', **coords)
#    dsout.copy_variable(dsin.ds, 'srfgeo')

#    print(dsout.ds)

#    print(dsout.ds.lat)
#    latitude = dsout.ds.lon
#    print(latitude)

################
# Write file

#    ofile = './test.nc'
#    dsout.write_netcdf(ofile)
