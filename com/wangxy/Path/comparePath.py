__author__ = 'wangxy'
#coding=utf8

from numpy import *

def loadVertexInfo():
	gc={}
	iter = open("/home/wangxy/data/path/vertexInfo.csv")
	for line in iter.readlines():
		strArr = line.strip().split(",",-1)
		gc[int(strArr[0])] = [float(strArr[1]), float(strArr[2])]
	return gc
path=[41,42,44,46,47,48,53,65,62,61,60,64,54]
path1=[41,42,44,46,47,48,53,65,62,61,60,64,54]
# path=[42,44,46,51,58,62,65,66,67,68,73,77]
# path1=[42,44,46,51,58,62,65,66,67,68,73,77]
path2=[42,45,46,67,52,58,62,65,66,67,76,77]
path3=[42,45,49,50,54,64,72,79,78,76,77]

def lonLat2Mercator(lon, lat):
	x = lon * 20037508.342789 / 180
	y = log(tan((90 + lat) * pi / 360)) / (pi / 180)
	y = y * 20037508.34789 / 180
	return (x, y)

def etlx(x, gc, index, length):
	info = gc.get(x,[0,0])
	xy=lonLat2Mercator(info[0],info[1])
	return [int(x), 1, int(xy[0]), int(xy[1]), int(index*1.0/length*100)]

def etldata(data,gc):
	info=[]
	for i in range(0,len(data)):
		info.append(etlx(data[i], gc, i+1, len(data)))
	return array(info)

gc = loadVertexInfo()
np = etldata(path, gc)
print 'np=',np
np1 = etldata(path1, gc)
print 'np1=',np1
np2 = etldata(path2, gc)
np3 = etldata(path3, gc)

def calcRsquare(yHat, yArr):
	m = shape(yHat)[0]
	avg = mean(yArr)
	yb = mat(ones((m,1)))*avg
	# print 'avg',avg
	# print 'yb',yb
	SSR = sum((yHat-yb.T).T*(yHat-yb.T))
	# print 'SSR=',SSR
	SST = sum((yArr-yb.T).T*(yArr-yb.T))
	# print 'SST=',SST
	return float(SSR/SST)

# 局部加权线性回归
def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    # print 'weights=', weights
    for j in range(m):                      #next 2 lines create weights matrix
        diffMat = testPoint - xMat[j,:]     #
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
	print 'weights=',weights
    xTx = xMat.T * (weights * xMat)
    # print 'xTx=',xTx,'  det=',linalg.det(xTx)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def lwlrTest(testArr,xArr,yArr,k=1.0):  #loops over all the data points and applies lwlr to each one
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat

# print 'z=',lwlr(np[:,1:4][9],np1[:,1:4],np1[:,4],10000)
path1 =  lwlrTest(np[:,1:4], np1[:,1:4], np1[:,4],200)
print 'path1=',path1
print 'np=',np[:,4]
# #
# r1 = calcRsquare(path1, np[:,4])
# print 'r1=',r1
# #
path2 =  lwlrTest(np[:,1:4], np2[:,1:4], np2[:,4],200)
print 'path2=',path2
print 'np=',np[:,4]
# #
# r2 = calcRsquare(path2, np[:,4])
# print 'r2=',r2
#
path3 =  lwlrTest(np[:,1:4], np3[:,1:4], np3[:,4],200)
print 'path3=',path3
print 'np=',np[:,4]
#
# r3 = calcRsquare(path3, np[:,4])
# print 'r3=',r3

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# X = [100, 205, 220, 480]
# Y = [1050, 1240, 1680, 1400]
# Z = [1, 2, 3, 4]
# ax.plot_trisurf(X, Y, Z)
ax.scatter(np[:,2],np[:,3],np[:,4], color='r')
ax.plot(np[:,2],np[:,3],np[:,4],color='r')

ax.scatter(np[:,2],np[:,3],path1, color='b')
ax.plot(np[:,2],np[:,3],path1,color='b')

ax.scatter(np[:,2],np[:,3],path2, color='y')
ax.plot(np[:,2],np[:,3],path2,color='y')

ax.scatter(np[:,2],np[:,3],path3, color='g')
ax.plot(np[:,2],np[:,3],path3,color='g')
plt.show()





