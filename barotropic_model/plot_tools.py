#!/usr/bin/env python

import os

import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm

import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point

#############################


class plot_tools:
    def __init__(self, central_longitude=0.):

        self.central_longitude = central_longitude

        self.trans = ccrs.PlateCarree()
        self.proj = ccrs.PlateCarree(central_longitude= \
                                       self.central_longitude,
                                     globe=None)

        self.fig = plt.figure(figsize=(9, 6))
        self.ax = plt.subplot(111, projection=self.proj)

        ###

        self.fs = 13
        self.title_fs = 14

#############################

    def settings(self, field, diff=False):

        cmap = plt.get_cmap('RdBu_r')
        levels = 10
        label = ''

        if field in ['t2m', 'TS']:
            label = 'Surface temperature [$^\circ$C]'
            cmap = plt.get_cmap('RdBu_r')
#            levels = np.linspace(-30., 30., 16)
            levels = [-30., -25., -20., -15., -10., -5.,
                      5., 10., 15., 20., 25., 30.]

            if diff is True:
                label = 'Surface temperature anomaly [$^\circ$C]'
                cmap = plt.get_cmap('RdBu_r')
                levels = [-18., -15., -12., -9., -6., -3.,
                          3., 6., 9., 12., 15., 18.]

        if field in ['topo', 'srfgeo']:
            label = 'Topography [m]'
            cmap = plt.get_cmap('RdBu_r')
            # levels = np.linspace(500., 5000., 10)
            levels = [1000., 2000., 3000., 4000., 5000.]

            if diff is True:
                label = 'Topography anomaly [m]'
                cmap = plt.get_cmap('RdBu_r')
                levels = np.linspace(-1000., 1000., 11)

        return cmap, levels, label

#############################

    def quick_plot(self, lats, lons, var,
                   levels=None, cmap=None, add_cyclic=False):

        if add_cyclic is True:
            var, lons = add_cyclic_point(var, coord=lons)

        if levels is None:
            levels = 10

        if cmap is None:
            cmap = plt.get_cmap('RdBu_r')

        cf = self.ax.contourf(lons, lats, var, levels,
                              cmap=cmap,
                              extend='both',
                              transform=self.trans)

        cbar = self.fig.colorbar(cf, shrink=0.75, extend='both',
                                 orientation='horizontal')

        self.ax.coastlines()
        self.ax.set_global()

        plt.show()

#   ### ### ### ### ### ### ### ### ### ### ###

    def plot_field(self, lats, lons,
                   var_cf=None, field_cf=None, diff_cf=False,
                   var_cr=None, field_cr=None, diff_cr=False,
                   title='',
                   save=False, ofile=None):

        # Make 2D lat and lon arrays
        #        lons, lats = np.meshgrid(lon, lat)

        ###

        if var_cf is not None:
            try:
                cmap_cf, levels_cf, label_cf = self.settings(field=field_cf,
                                                             diff=diff_cf)
                norm_cf = BoundaryNorm(levels_cf, ncolors=cmap_cf.N, clip=True)

            except Exception:
                levels_cf = 10
                cmap_cf = plt.get_cmap('RdBu_r')

            cf = self.ax.contourf(lons, lats, var_cf, levels_cf,
                                  cmap=cmap_cf, norm=norm_cf,
                                  extend='both',
                                  transform=self.trans)

            ax0 = self.ax.get_position()
            loc_cbar = self.fig.add_axes([ax0.x0, 0.15, ax0.width, 0.03])
            cb_ax = self.fig.add_axes(loc_cbar)

            try:
                cbar_cf = self.fig.colorbar(cf, cax=cb_ax, ticks=levels_cf,
                                            extend='both',
                                            orientation='horizontal')
                """
                cbar_cf.ax.tick_params(direction='inout',
                                       labelsize=self.fs,
                                       length=8,
                                       width=1,
                                       colors='k',
                                       grid_color='k',
                                       grid_alpha=0.5)
                """
            except Exception:
                cbar_cf = self.fig.colorbar(cf, shrink=0.75,
                                            extend='both',
                                            orientation='horizontal')
            else:
                pass

            try:
                cbar_cf.set_label(label=label_cf, size=16)
            except Exception:
                pass

        # ## ### #### ### ## #
        # Contour plot
        if var_cr is not None:
            try:
                cmap_cr, levels_cr, label_cr = self.settings(field=field_cr,
                                                             diff=diff_cr)
            except Exception:
                pass

            cr = self.ax.contour(lons, lats, var_cr, levels_cr,
                                 colors='k',
                                 transform=self.trans)

###

            self.ax.set_title(title, loc='left',
                              fontsize=self.title_fs, fontweight='bold')

        self.ax.coastlines()
        self.ax.set_global()
#        self.ax.gridlines()

###

        if save is True:
            plt.savefig('{}.pdf'.format(ofile),
                        dpi=None, facecolor='w', edgecolor='w',
                        orientation='portrait', papertype=None,
                        format=None, transparent=False,
                        bbox_inches='tight', pad_inches=0.1)

        else:
            plt.show()

        self.fig.clf()


#############################


if __name__ == "__main__":

    pass


#############################
# # === END OF SCRIPT === # #
#############################
