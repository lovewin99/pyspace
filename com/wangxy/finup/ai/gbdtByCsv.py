#!usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
from sklearn import metrics
import numpy as np
import cPickle as pickle
from sklearn.datasets import load_svmlight_file

# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier(train_x, train_y):
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=200)
    model.fit(train_x, train_y)
    return model

if __name__ == '__main__':
    x = []
    y = []
    file = open("/Users/wangxy/Desktop/qztest1.csv")
    for fr in file.readlines():
        str = fr.replace("NA", "")
        strArr = str.split(",")
        y.append(strArr[1])
        x.append(strArr[1:])
    model = gradient_boosting_classifier(x, y)
    # t_x = np.ndarray(x)
    # t_y = np.ndarray(y)