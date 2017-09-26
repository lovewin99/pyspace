#coding=utf8
__author__ = 'wangxy'

from numpy import *

# 局部加权线性回归
def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    # print 'weights=', weights
    for j in range(m):                      #next 2 lines create weights matrix
        diffMat = testPoint - xMat[j,:]     #
        # print 'diffmat=', diffMat
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    print 'ws=', ws
    return testPoint * ws

def lwlrTest(testArr,xArr,yArr,k=1.0):  #loops over all the data points and applies lwlr to each one
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat


def calcRsquare(yHat, yArr):
	m = shape(yHat)[0]
	avg = mean(yArr)
	print 'm=',m
	yb = mat(ones((m,1)))*avg
	print 'mean=',mean(yArr)
	SSR = sum((yHat-yb.T).T*(yHat-yb.T))
	SST = sum((yArr-yb.T).T*(yArr-yb.T))
	print 'SSR=',SSR,'   SST=',SST
	return float(SSR/SST)

a = mat((1,2,2,4))
b = mat((1,2,3,4))

print calcRsquare(a.T, b.T)
