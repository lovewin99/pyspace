__author__ = 'wangxy'
#coding=utf-8

from numpy import *

# 经纬度转墨卡托
def lonLat2Mercator(lon, lat):
	x = lon * 20037508.342789 / 180
	y = log(tan((90 + lat) * pi / 360)) / (pi / 180)
	y = y * 20037508.34789 / 180
	return (x,y)

def loaddata(path):
	lines=[]
	fr = open(path)
	for line in fr.readlines():
		strArr = line.split()
		lines.append(strArr)
	return lines

strArr1 = array(loaddata("/home/wangxy/data/ex0.txt"))
# print array(strArr1)[:,0:2]

def etl(data):
	(x,y) = lonLat2Mercator(float(data[0]),float(data[1]))
	return [x,y,data[2]]

print map(etl, strArr1)

def loadGc(path):
	gcMap={}
	fr = open(path)
	for line in fr.readlines():
		strArr = line.split(",", -1)
		key = strArr[11]+","+strArr[7]
		value = (strArr[38], strArr[44])
		gcMap[key]=value
