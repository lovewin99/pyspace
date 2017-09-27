# -*- coding: utf-8 -*-
"""
@File  : SampleData.py
@Author: wangxy
@Date  : 2017/9/27
@Desc  : 
"""

from sklearn.cross_validation import train_test_split

if __name__ == "__main__":
    file = open("/Users/wangxy/Desktop/output/part-00000")
    X = []; y = []; all = []
    X_train = []; y_train = []; X_test = []; y_test = []
    for fr in file.readlines():
        strArr = fr.strip().split(" ")
        all = strArr
        X.append(strArr[1:])
        y.append(strArr[0])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

    print 'len1=', len(X_train), "  len2=",len(X_test),'  len3=',len(y_train),'  len4=',len(y_test)
    train_data = zip(y_train, X_train)
    test_data = zip(y_test, X_test)

    tr1 = map(lambda (m, n): m + ' ' + ' '.join(n), train_data)
    tr2 = "\n".join(tr1)

    te1 = map(lambda (m, n): m + ' ' + ' '.join(n), test_data)
    te2 = "\n".join(te1)


    file_object = open('/Users/wangxy/Desktop/train_data', 'w')
    file_object.write(tr2)
    file_object.close()

    file_object = open('/Users/wangxy/Desktop/test_data', 'w')
    file_object.write(te2)
    file_object.close()

    file.close()

