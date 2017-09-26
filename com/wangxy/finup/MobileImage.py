#coding=utf8
__author__ = 'wangxy'

import numpy as np
import matplotlib.pyplot as plt


yuqi = open("/Users/wangxy/data/finup/kn78/kn78data.txt")
noyuqi = open("/Users/wangxy/data/finup/kn78/kn78nodata.txt")
mixdata = []

yuqiApplyNo = []
yuqidata = []
for fr in yuqi.readlines():
    strArr = fr.strip().split(',')
    yuqiApplyNo.append(strArr[0])
    mixdata.append(strArr[1:])

yuqilen = len(mixdata)

noyuqiApplyNo = []
noyuqidata = []
for fr in noyuqi.readlines():
    strArr = fr.strip().split(',')
    noyuqiApplyNo.append(strArr[0])
    mixdata.append(strArr[1:])

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(1, 1, 1)
k11 = [x[9] for x in mixdata]
k12 = [x[10] for x in mixdata]

# ax.plot(k11[0:yuqilen], k12[0:yuqilen],'w',markerfacecolor='r', marker='.')
ax.plot(k11[yuqilen:len(mixdata)], k12[yuqilen:len(mixdata)],'w',markerfacecolor='b', marker='.')

# title = ["numCall1","freeCall1","morningCall1","numCall3","earlyMoringCall3","numCall6","morningCall6",
#          "nightCall6","calling6","called6"]
#
# for i in range(2, 12):
#     fig = plt.figure(figsize=(14, 8))
#     ax = fig.add_subplot(1, 1, 1)
#     kk1 = [x[i] for x in mixdata]
#     ax.plot(kk1[0:yuqilen],'w',markerfacecolor='r', marker='.')
#     ax.plot(kk1[yuqilen:len(mixdata)],'w',markerfacecolor='b', marker='.')
#     ax.set_title(title[i-2])


# ax.plot(kk[0:yuqilen],'w',markerfacecolor='r', marker='.')
# ax.plot(kk[yuqilen:len(kk)],'w',markerfacecolor='b', marker='.')



plt.show()