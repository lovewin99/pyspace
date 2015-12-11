__author__ = 'wangxy'
#coding=utf8

import numpy as np
import matplotlib.pyplot as plt

xData = np.arange(0, 10, 1)
print xData
yData1 = xData.__pow__(2.0)
print yData1
yData2 = np.arange(15, 61, 5)
print yData2
plt.figure(num=1, figsize=(8, 6))
plt.title('Plot 1', size=14)
plt.xlabel('x-axis', size=14)
plt.ylabel('y-axis', size=14)
# 画线
plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
plt.legend(loc='upper left')
# 描点
# plt.scatter(xData, yData1, c='b',s=50)
# plt.scatter(xData, yData2, c='r',s=50)
#plt.savefig('/home/wangxy/data/plot1.png', format='png')
plt.show()