__author__ = 'wangxy'
#coding=utf8

from numpy import *

# 经纬度转墨卡托
def lonLat2Mercator(lon, lat):
	x = lon * 20037508.342789 / 180
	y = log(tan((90 + lat) * pi / 360)) / (pi / 180)
	y = y * 20037508.34789 / 180
	return (x,y)
