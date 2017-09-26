#coding=utf8
__author__ = 'wangxy'

import numpy as np
import matplotlib.pyplot as plt

data = open("/Users/wangxy/Desktop/approval/part-00000")

y = []
x = []

for fr in data.readlines():
    strArr = fr.strip().split(',')
    y.append(strArr[1])
    x.append(strArr[0])

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(1, 1, 1)

ax.scatter(x, y, c='r',s=20)

plt.show()