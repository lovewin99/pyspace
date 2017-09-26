#coding=utf8
__author__ = 'wangxy'

import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin

yuqi = open("/Users/wangxy/Desktop/taobao_trans_repaid_feature.info")
noyuqi = open("/Users/wangxy/Desktop/taobao_trans_over_dure_feature.info")

yuqiAppNo = []
mixdata = []
for fr in yuqi.readlines():
    strArr = fr.strip().split('\001')
    yuqiAppNo.append(strArr[0])
    mixdata.append(strArr[1:])

yuqilen = len(mixdata)

noyuqiAppNo = []
for fr in noyuqi.readlines():
    strArr = fr.strip().split('\001')
    noyuqiAppNo.append(strArr[0])
    mixdata.append(strArr[1:])

noyuqilen = len(mixdata) - yuqilen
print mixdata

# np.any(np.isnan(np.array(mixdata)))

# np.all(np.isfinite(mixdata))

# k_means = KMeans(init='k-means++', n_clusters=8, n_init=10)
# k_means.fit(mixdata)
#
# k_means_labels = pairwise_distances_argmin(mixdata, k_means.cluster_centers_)
#

model = AgglomerativeClustering(affinity="cosine",n_clusters=10,linkage="complete")
y = model.fit_predict(mixdata)

a = y[:yuqilen]
b = y[yuqilen:]

# a = k_means_labels[:yuqilen]
# b = k_means_labels[yuqilen:]
#
# a = k_means_labels[:yuqilen]
# b = k_means_labels[yuqilen:]
#
print 'len=',len(a),'  1=',len([i for i in a if i == 1]),'  0=',len([i for i in a if i == 0]),'  2=',len([i for i in a if i == 2]),'  3=',len([i for i in a if i == 3]),'  4=',len([i for i in a if i == 4]),'  5=',len([i for i in a if i == 5]),'  6=',len([i for i in a if i == 6]),'  7=',len([i for i in a if i == 7]),'  8=',len([i for i in a if i == 8]),'  9=',len([i for i in a if i == 9]),'  10=',len([i for i in a if i == 10])
print 'len=',len(b),'  1=',len([i for i in b if i == 1]),'  0=',len([i for i in b if i == 0]),'  2=',len([i for i in b if i == 2]),'  3=',len([i for i in b if i == 3]),'  4=',len([i for i in b if i == 4]),'  5=',len([i for i in b if i == 5]),'  6=',len([i for i in b if i == 6]),'  7=',len([i for i in b if i == 7]),'  8=',len([i for i in b if i == 8]),'  9=',len([i for i in b if i == 9]),'  10=',len([i for i in b if i == 10])

