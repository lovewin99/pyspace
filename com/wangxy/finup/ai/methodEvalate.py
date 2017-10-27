# -*- coding: utf-8 -*-
"""
@File  : methodEvalate.py
@Author: wangxy
@Date  : 2017/9/28
@Desc  : 通过预测值评估算法
"""

if __name__ == '__main__':
    rfilename = "/Users/wangxy/Desktop/test_data"
    pfilename = "/Users/wangxy/Desktop/pypredict.txt"
    realfile = open(rfilename)
    predictfile = open(pfilename)

    positive = '0'; negative = '1'

    y_real = []; y_predict = []
    for fr in realfile.readlines():
        y_real.append(fr.strip().split(" ")[0])

    for fr in predictfile.readlines():
        y_predict.append(fr.strip().split(" ")[0])

    if len(y_real) == len(y_predict):
        TP = 0.0; FN = 0.0; FP = 0.0; TN = 0.0
        print type(TP)
        for i in range(0, len(y_real)):
            if y_real[i] == positive and y_predict[i] == positive:
                TP += 1
            if y_real[i] == positive and y_predict[i] == negative:
                FN += 1
            if y_real[i] == negative and y_predict[i] == positive:
                FP += 1
            if y_real[i] == negative and y_predict[i] == negative:
                TN += 1

        TPR = TP / (TP + FN)
        FPR = FP / (TN + FP)
        P = TP / (TP + FP)
        R = TP / (TP + FN)

        print '真正率 TPR = ', TPR
        print '假正率 FPR = ', FPR
        print '精度 P = ', P
        print '召回率 R = ', R

    else:
        print 'lens not matching'

