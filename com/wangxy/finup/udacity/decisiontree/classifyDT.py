# -*- coding: utf-8 -*-
"""
@File  : classifyDT.py
@Author: wangxy
@Date  : 2017/10/12
@Desc  : 
"""


def classify(features_train, labels_train):
    ### your code goes here--should return a trained decision tree classifer
    # >> from sklearn import tree
    # >> > X = [[0, 0], [1, 1]]
    # >> > Y = [0, 1]
    # >> > clf = tree.DecisionTreeClassifier()
    # >> > clf = clf.fit(X, Y)
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split=50)
    clf = clf.fit(features_train, labels_train)


    return clf