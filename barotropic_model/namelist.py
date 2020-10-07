#!/usr/bin/env python

"""
Namelist for barotropic model
"""

import os

#############################

# Time stepping


# Spectral operators
trunc = None        # Truncation (if None, defaults to # latitudes)
rsphere = 6.3712e6  # Planetary radius
legfunc = 'stored'  # Legendre functions


# I/O
