#coding=utf8
__author__ = 'wangxy'

import numpy as np
import matplotlib.pyplot as plt


yuqi = open("/Users/wangxy/Desktop/creditcarddata/part-00000")
# noyuqi = open("/Users/wangxy/Desktop/t2/part-00000")
# noyuqi = open("/Users/wangxy/data/finup/kn78/kn78nodata.txt")
mixdata = []

y = []
x1 = []
x2= []
for fr in yuqi.readlines():
    strArr = fr.strip().split(',')
    if int(strArr[2]) < 300:
        x1.append(strArr[1])
        y.append(strArr[2])
        x2.append(strArr[4])

# m = []
# n1 = []
# n2 = []
# for fr in noyuqi.readlines():
#     strArr = fr.strip().split(',')
#     if int(strArr[2]) < 300:
#         n1.append(strArr[1])
#         m.append(strArr[2])
#         n2.append(strArr[3])

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(1, 1, 1)
# k11 = [x[9] for x in mixdata]
# k12 = [x[10] for x in mixdata]

# ax.plot(k11[0:yuqilen], k12[0:yuqilen],'w',markerfacecolor='r', marker='.')
# ax.plot(x1, y,'w',markerfacecolor='b', marker='.')
# ax.plot(x2, y,'w',markerfacecolor='r', marker='.')
# ax.plot(x1, x2,'w',markerfacecolor='g', marker='.')
ax.scatter(x2, y, c='r',s=20)
# ax.scatter(n2, m, c='b',s=10)


plt.show()