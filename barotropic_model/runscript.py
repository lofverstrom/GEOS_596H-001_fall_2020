#!/usr/bin/env python

from barotropic import barotropic

############################


############################

if __name__ == "__main__":

    model = barotropic()

    print(model.__doc__)

    print(model.integrate_linear_dynamics.__doc__)

#    print(barotropic().__doc__)

#############################
### +++ END OF SCRIPT +++ ###
#############################
