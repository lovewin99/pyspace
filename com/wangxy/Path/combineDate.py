__author__ = 'wangxy'
#coding=utf8

from numpy import *
from utils.cooTranslate import *
import matplotlib.pyplot as plt

# 加载工参表
def loadGc(path):
	gcMap={}
	fr = open(path)
	for line in fr.readlines():
		strArr = line.split(",", -1)
		key = strArr[11]+","+strArr[7]
		value = lonLat2Mercator(float(strArr[38]), float(strArr[44]))
		gcMap[key]=value

# 加载路点
def loadVertexAndDraw(path, plt):
	lines={}
	fr = open(path)
	for line in fr.readlines():
		strArr = line.split(",",-1)
		(x,y) = lonLat2Mercator(float(strArr[1]), float(strArr[2]))
		plt.scatter(int(x), int(y), c='b',s=5)
		# lines.append([strArr[0], x, y])
		plt.text(int(x), int(y), strArr[0])
		lines[strArr[0]] = (int(x),int(y))
	return lines

# 加载路网
def loadEdgeNetAndDraw(path, vertex, plt):
	fr = open(path)
	edgeflag={}
	for line in fr.readlines():
		strArr = line.split(",",-1)
		if strArr[2] not in edgeflag:
			edgeflag[strArr[2]]=1
			srcPosition = vertex[strArr[0]]
			dstPosition = vertex[strArr[1]]
			plt.annotate("",xy=dstPosition, xytext=srcPosition,arrowprops=dict(facecolor='blue', shrink=0.2))

# 加载路线1
def loadData1(path, plt):
	linePath=[]
	fr = open(path)
	first = True
	for line in fr.readlines():
		strArr = line.split(",", -1)
		(x,y) = lonLat2Mercator(float(strArr[1]),float(strArr[2]))
		if first :
			plt.scatter(int(x),int(y),c='red',s=130)
			first=False
		linePath.append([int(x),int(y)])
	return linePath


# gclib = loadGc("/home/wangxy/data/shanghai20141204.csv")

vertexInfo = loadVertexAndDraw("/home/wangxy/data/path/vertexInfo.csv", plt)

loadEdgeNetAndDraw("/home/wangxy/data/path/edgeInfo.csv",vertexInfo, plt)

# line1 = array(loadData1("/home/wangxy/data/path/1seq.csv",plt))
line2 = array(loadData1("/home/wangxy/data/path/tmpseq.csv",plt))

# plt.plot(line1[:,0], line1[:,1], color='g', linestyle='--', label='y1 data')
for idx in range(0,line2.size/2-2):
	plt.annotate("",xy=(line2[idx+1,0], line2[idx+1,1]), xytext=(line2[idx,0], line2[idx,1]),arrowprops=dict(facecolor='red', shrink=0.05))
# plt.plot(line2[:,0], line2[:,1], color='r', linestyle='--', label='y1 data')
plt.scatter(line2[-1,0],line2[-1,1],c='g',s=130)
plt.scatter(line2[:,0],line2[:,1],c='y',s=50)

plt.show()
