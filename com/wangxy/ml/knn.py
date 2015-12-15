__author__ = 'wangxy'
#coding=utf8
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

# 基本样例代码
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # print 'dataSetSize=', dataSetSize
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    # print 'diffMat=', diffMat
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    # print 'sqDistances=', sqDistances
    distances = sqDistances**0.5
    # argsort 返回排序后的下标
    sortedDistIndicies = distances.argsort()
    # print 'sortedDistIndicies=',sortedDistIndicies
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

# group,labels = createDataSet()
# print 'group=',group,'  labels=',labels
# print classify0([0,0], group, labels, 3)

# 维度分析与可视化
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

datingDataMat,datingLabels = file2matrix('/home/wangxy/data/digits/datingTestSet.txt')
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
# # ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
# plt.show()

# 归一化
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    # print 'minVals=',minVals
    maxVals = dataSet.max(0)
    # print 'maxVals=',maxVals
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    # print 'shape=',shape(dataSet)
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    # print 'tile=',tile(ranges, (m,1))
    return normDataSet, ranges, minVals

normMat, ranges, minVals = autoNorm(datingDataMat)
# print 'normMat=',normMat

# 实测分类器准确度　数据五五分
def datingClassTest():
    hoRatio = 0.50      #hold out 10%
    datingDataMat,datingLabels = file2matrix('/home/wangxy/data/digits/datingTestSet.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))
    print errorCount

datingClassTest()

# 单条分类器
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("liters of ice cream consumed per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('/home/wangxy/data/digits/datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    print "You will probably like this person: ", resultList[classifierResult - 1]

#classifyPerson()
