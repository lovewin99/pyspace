#coding=utf8
__author__ = 'wangxy'


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = [100, 205, 220, 480]
Y = [1050, 1240, 1680, 1400]
Z = [1, 2, 3, 4]
# ax.plot_trisurf(X, Y, Z)
ax.scatter(X,Y,Z, color='r')
ax.plot(X,Y,Z)
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# ax = plt.subplot(111)
# t = np.arange(0.0, 5., 0.01)
# s = np.cos(2*np.pi*t)
# line, = plt.plot(t, s, linewidth = 3)
# # plt.annotate('local max', xy = (2, 1), xytext = (3, 1.5), arrowprops = dict(facecolor = 'black', shrink = 0.1))
# plt.annotate('local max', xy = (2, 1), xytext = (2, 1))
# plt.ylim(-2, 2)
# plt.show()