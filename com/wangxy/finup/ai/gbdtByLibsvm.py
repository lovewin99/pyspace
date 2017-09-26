#!usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
from sklearn import metrics
import numpy as np
import cPickle as pickle
from sklearn.externals import joblib
import pickle as pickle
from sklearn.datasets import load_svmlight_file

# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier(train_x, train_y):
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=8000, max_depth=6, learning_rate=0.01)
    model.fit(train_x, train_y)
    return model

if __name__ == '__main__':
    # t_X,t_y=load_svmlight_file("/Users/wangxy/train1.data")
    t_X, t_y = load_svmlight_file("/Users/wangxy/Desktop/output/part-00000", dtype=np.string_)
    print '1111'
    start_time = time.time()
    model = gradient_boosting_classifier(t_X, t_y)
    # pickle.dump(model, open("/Users/wangxy/Desktop/model.txt", 'wb'))
    print 'training took %fs!' % (time.time() - start_time)
    joblib.dump(model, "train_model.m")
    print 'all took %fs!' % (time.time() - start_time)
    # print type(t_X)
