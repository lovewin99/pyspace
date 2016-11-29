__author__ = 'wangxy'
#coding=utf8

from numpy import *

def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float,line) for line in stringArr]
    return mat(datArr)

def pca(dataMat, topNfeat=9999999):
    # 计算平均值
    meanVals = mean(dataMat, axis=0)
    # 去除平均值
    meanRemoved = dataMat - meanVals #remove mean
    # 计算协方差
    covMat = cov(meanRemoved, rowvar=0)
    # print covMat
    # [[ 1.05198368  1.1246314 ]
    # [ 1.1246314   2.21166499]]
    # 计算特征值　特征向量
    eigVals,eigVects = linalg.eig(mat(covMat))
    print 'eigVals=', eigVals
    print 'eigVects=', eigVects
    # 排序　从小到大
    eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest
    print 'eigValInd=', eigValInd
    # 取特征值最大的几个
    eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions
    print 'eigValInd=',eigValInd
    #　特征值大的对应的特征向量
    redEigVects = eigVects[:,eigValInd]       #reorganize eig vects largest to smallest
    print 'redEigVects=', redEigVects
    # 降维后的矩阵
    lowDDataMat = meanRemoved * redEigVects #transform data into new dimensions
    # 数据转换变换到原空间中
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat


dataMat = loadDataSet('/home/wangxy/data/testSetpca.txt')
lowDMat, reconMat = pca(dataMat, 1)

print 'lowDMat=', lowDMat
print 'reconMat=', reconMat