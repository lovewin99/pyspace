# -*- coding: utf-8 -*-
"""
@File  : studentMain.py
@Author: wangxy
@Date  : 2017/10/12
@Desc  : 
"""

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())

from sklearn.metrics import accuracy_score
print accuracy_score(clf.predict(features_test), labels_test)