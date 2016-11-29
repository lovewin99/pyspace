__author__ = 'wangxy'
#coding=utf-8

from numpy import *

# 经纬度转墨卡托
def lonLat2Mercator(lon, lat):
	x = lon * 20037508.342789 / 180
	y = log(tan((90 + lat) * pi / 360)) / (pi / 180)
	y = y * 20037508.34789 / 180
	return (x,y)

# 加载路点
def loadDataAndEtl1(path):
	lines=[]
	fr = open(path)
	for line in fr.readlines():
		strArr = line.split()
		(x,y) = lonLat2Mercator(float(strArr[1]), float(strArr[2]))
		lines.append([strArr[0], x, y])
	return lines

# 加载工参表
def loadGc(path):
	gcMap={}
	fr = open(path)
	for line in fr.readlines():
		strArr = line.split(",", -1)
		key = strArr[11]+","+strArr[7]
		value = lonLat2Mercator(float(strArr[38]), float(strArr[44]))
		gcMap[key]=value

gclib = loadGc("/home/wangxy/data/shanghai20141204.csv")

strArr1 = array(loadDataAndEtl1("/home/wangxy/data/ex0.txt"))
# print array(strArr1)[:,0:2]

def etl(data):
	(x,y) = lonLat2Mercator(float(data[0]),float(data[1]))
	return [x,y,data[2]]

print map(etl, strArr1)


