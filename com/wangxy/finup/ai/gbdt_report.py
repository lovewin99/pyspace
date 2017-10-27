# -*- coding: utf-8 -*-
"""
@File  : gbdt_report.py
@Author: wangxy
@Date  : 2017/10/24
@Desc  : 
"""

import sys
import os
import time
from sklearn import metrics
import numpy as np
import cPickle as pickle
from sklearn.externals import joblib
import pickle as pickle
from sklearn.datasets import load_svmlight_file
from sys import argv

# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier(train_x, train_y):
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=1000, max_depth=6, learning_rate=0.01)
    model.fit(train_x, train_y)
    return model

if __name__ == '__main__':

    t_X, t_y = load_svmlight_file("/Users/wangxy/Desktop/train.txt", dtype=np.string_)
    print type(t_X)
    start_time = time.time()
    model = gradient_boosting_classifier(t_X, t_y)
    print 'all took %fs!' % (time.time() - start_time)
    X, y = load_svmlight_file("/Users/wangxy/Desktop/test/test1.csv")
    print type(X)
    a1 = X.todense()
    print type(a1)
    print type(y)
    yp = model.predict(a1)
    print metrics.roc_auc_score(y, yp)

