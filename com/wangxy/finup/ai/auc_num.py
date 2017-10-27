# -*- coding: utf-8 -*-
"""
@File  : auc_num.py
@Author: wangxy
@Date  : 2017/10/25
@Desc  : 
"""

from sklearn.metrics import auc,roc_auc_score

if __name__== '__main__':
    x = []
    y = []
    # file = open("/Users/wangxy/Desktop/gbdttest3/predict/all.txt")
    file = open("/Users/wangxy/Desktop/mllibpredict/mllibprd3/all.txt")
    for fr in file.readlines():
        strArr = fr.strip().split(',', -1)
        x.append(float(strArr[0]))
        y.append(float(strArr[1]))
        # if float(strArr[1]) > 0:
        #     y.append(1.0)
        # else:
        #     y.append(0.0)

    print roc_auc_score(x, y)