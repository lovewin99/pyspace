#coding=utf8
__author__ = 'wangxy'

import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.datasets.samples_generator import make_blobs

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

print mixdata

noyuqiApplyNo = []
noyuqidata = []
for fr in noyuqi.readlines():
    strArr = fr.strip().split(',')
    noyuqiApplyNo.append(strArr[0])
    mixdata.append(strArr[1:])

noyuqilen = len(mixdata) - yuqilen

k_means = KMeans(init='k-means++', n_clusters=3, n_init=10)
k_means.fit(mixdata)

k_means_labels = pairwise_distances_argmin(mixdata, k_means.cluster_centers_)

a = k_means_labels[:yuqilen]
b = k_means_labels[yuqilen:]

c = a == 0

print np.array(yuqiApplyNo)[c]

print 'len=',len(a),'  1=',len([i for i in a if i == 1]),'  0=',len([i for i in a if i == 0]),'  2=',len([i for i in a if i == 2])
print 'len=',len(b),'  1=',len([i for i in b if i == 1]),'  0=',len([i for i in b if i == 0]),'  2=',len([i for i in b if i == 2])



# print 'mixdata=',mixdata
# print 'yuqiApplyNo=',yuqiApplyNo