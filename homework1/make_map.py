import numpy as np
import netCDF4 as nc

import glob

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

data = nc.Dataset('data/emp.cdf', 'r')

print(data.variables['emp'])
