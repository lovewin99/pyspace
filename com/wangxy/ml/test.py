__author__ = 'wangxy'

from numpy import *
import regTrees
import numpy as np
import matplotlib.pyplot as plt

data = mat(regTrees.loadDataSet('/home/wangxy/data/sine.txt'))
# plt.scatter(data[:,0], data[:,1], s=5)
plt.plot(data[:,0], data[:,1], ".")
plt.show()
