# -*- coding: utf-8 -*-
"""
@File  : xgboostTest.py
@Author: wangxy
@Date  : 2017/10/10
@Desc  : 
"""

import xgboost as xgb
# read in data
dtrain = xgb.DMatrix('/usr/local/xgboost/demo/data/agaricus.txt.train')
dtest = xgb.DMatrix('/usr/local/xgboost/demo/data/agaricus.txt.test')
# specify parameters via map
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
num_round = 2
bst = xgb.train(param, dtrain, num_round)
# make prediction
preds = bst.predict(dtest)

print dtrain
print '!!!!!!!!'
print preds
