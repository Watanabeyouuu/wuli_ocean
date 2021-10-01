import numpy as np
import netCDF4 as nc

import glob

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


def draw_map(file_obj):
    data_name = ''
    long_name = ''
    units = ''
    for i in file_obj.variables.keys():
        name = file_obj.variables[i]  # 文件中元素名
        long_name = name.long_name  # 文件中详细名
        units = name.units  # 文件中单位名
        data_name = i

    lon = file_obj.variables['X'][:]
    lat = file_obj.variables['Y'][:]
    time = file_obj.variables['T'][:]
    data = file_obj.variables[data_name][:]

    # print(lon.min(), lon.max(), lon.mean())
    # print(lat.min(), lat.max(), lat.mean())

    lon0 = lon.mean()
    lat0 = lat.mean()
    m = Basemap(llcrnrlon=lon.min(), llcrnrlat=lat.min(), urcrnrlon=lon.max(), urcrnrlat=lat.max())
    m.drawparallels(np.arange(-90., 91., 20.), labels=[1, 0, 0, 0], fontsize=10, color='none')
    m.drawmeridians(np.arange(-180., 181., 40.), labels=[0, 0, 0, 1], fontsize=10, color='none')
    m.drawcoastlines()

    lon, lat = np.meshgrid(lon, lat)
    xi, yi = m(lon, lat)
    bm = m.contourf(lon, lat, data[0, :, :])  # 填充匹配数据
    cd = m.contour(xi, yi, data[0, :, :], colors='k')  # 画等温线
    cb = m.colorbar(bm, location='bottom', pad="10%")  # 颜色图例
    cb.set_label(units)
    plt.clabel(cd, inline=True, fmt='%1.0f', fontsize=8, colors='k')
    plt.title(long_name)
    plt.show()


if __name__ == "__main__":
    f_name = glob.glob(r'data/*.cdf')
    print(f_name)
    for n in f_name:
        file_obj = nc.Dataset(n)
        draw_map(file_obj)
