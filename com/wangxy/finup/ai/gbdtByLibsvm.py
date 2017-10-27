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
from sys import argv

# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier(train_x, train_y):
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=8000, max_depth=6, learning_rate=0.01)
    model.fit(train_x, train_y)
    return model

if __name__ == '__main__':
    modelfile = "train_modelp.m"
    if (argv[1] == '1'):
        # t_X,t_y=load_svmlight_file("/Users/wangxy/train1.data")
        t_X, t_y = load_svmlight_file("/Users/wangxy/Desktop/train_data", dtype=np.string_)
        print type(t_X)
        print '1111'
        start_time = time.time()
        model = gradient_boosting_classifier(t_X, t_y)
        pickle.dump(model, open(modelfile, 'wb'))
        print 'training took %fs!' % (time.time() - start_time)
        # joblib.dump(model, modelfile)
        print 'all took %fs!' % (time.time() - start_time)
        # print type(t_X)
    else:
        rfile = "/Users/wangxy/Desktop/pypredict.txt"
        t_X, t_y = load_svmlight_file("/Users/wangxy/Desktop/test_data")
        # print t_y
        # print t_X
        pkfile2 = open(modelfile, 'rb')
        # model = joblib.load(modelfile)
        model = pickle.load(pkfile2)
        print type(t_X)
        # print t_X
        a1 = t_X.todense()
        y = model.predict(a1)
        y1 = [str(int(x)) for x in y]
        file_object = open(rfile, 'w')
        file_object.write("\n".join(y1))
        file_object.close()




