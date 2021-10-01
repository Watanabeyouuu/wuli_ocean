import netCDF4 as nc
import numpy as np
import matplotlib.pylab as plt

# from moviepy.editor import ImageSequenceClip

# 读取文件
data = nc.Dataset('data/emp.cdf', 'r')
data2 = nc.Dataset('data/shortrad.cdf', 'r')
data3 = nc.Dataset('data/longrad.cdf', 'r')
data4 = nc.Dataset('data/netheat.cdf', 'r')
data5 = nc.Dataset('data/precip.cdf', 'r')

# 提取各维度信息
lat = data.variables['X'][:].data
lon = data.variables['Y'][:].data
time = data.variables['T'][:].data
emp = data.variables['emp'][:].data
shortrad = data2.variables['shortrad'][:].data
longrad = data3.variables['longrad'][:].data
netheat = data4.variables['netheat'][:].data
precip = data5.variables['precip'][:].data

# 消去陆地值
# shortrad[shortrad < -1e5] = None
# emp[emp < -1e5] = None
# longrad[longrad < -1e5] = None
# netheat[netheat < -1e5] = None
# precip[precip < -1e5] = None

# print(emp[0, :, :].shape)
# print(lat)
# 十二个月的值 可以依次保存fig 各标题可以自定义
for i in range(12):
    print(lat.min())
    C = plt.contour(lat, lon, precip[i, :, :], 15, colors='black', linewidths=.5)
    Cf = plt.contourf(lat, lon, precip[i, :, :], 45, levels=np.linspace(-2, 9))

    plt.clabel(C, inline=0, fmt='%.2f')
    cb = plt.colorbar(Cf)
    cb.set_label('Precip mm/(3h)', fontsize=15)
    plt.ylabel('longitude', fontsize=15)
    plt.title('Global Distribution of Precip', fontsize=24)
    plt.show()

# 用以下C Cf替换上文
'''
C=plt.contour(lat,lon,shortrad[i,:,:],15,colors='black',linewidths=.5)
Cf=plt.contourf(lat,lon,shortrad[i,:,:],45,levels=np.linspace(0,405))#,cmap='jet')
C=plt.contour(lat,lon,longrad[i,:,:],15,colors='black',linewidths=.5)
Cf=plt.contourf(lat,lon,longrad[i,:,:],45,levels=np.linspace(0,210))
C=plt.contour(lat,lon,netheat[i,:,:],15,colors='black',linewidths=.5)
Cf=plt.contourf(lat,lon,netheat[i,:,:],45,levels=np.linspace(-600,400))
C=plt.contour(lat,lon,precip[i,:,:],15,colors='black',linewidths=.5)
Cf=plt.contourf(lat,lon,precip[i,:,:],45,levels=np.linspace(-2,9))
C=plt.contour(lat,lon,emp[i,:,:],15,colors='black',linewidths=.5)
Cf=plt.contourf(lat,lon,emp[i,:,:],45,levels=np.linspace(-10.5,5))
'''

# 合成GIF 需要debug
'''
img_names = ['./imgs/'+str(i)+'.png' for i in range(1,13)]
img_names.reverse()
clip = ImageSequenceClip(img_names,fps=1)
clip.write_gif('demo.gif')
'''
