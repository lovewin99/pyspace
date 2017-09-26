#coding=utf8
__author__ = 'wangxy'

import numpy as np
from sklearn.cross_validation import train_test_split

X = []
Y = []

file1 = open("/Users/wangxy/Desktop/overduedata.txt")
for fr in file1.readlines():
    strArr = fr.strip().split(',')
    Y.append(strArr[0])
    X.append(strArr[2:])
file1.close()

file2 = open("/Users/wangxy/Desktop/duedata.txt")
for fr in file2.readlines():
    strArr = fr.strip().split(',')
    Y.append(strArr[0])
    X.append(strArr[2:])
file2.close()

# file3 = open("/Users/wangxy/Desktop/mixdata/part-000002")
# for fr in file3.readlines():
#     strArr = fr.strip().split(',')
#     Y.append(strArr[0])
#     X.append(strArr[2:])
# file3.close()
#
# file4 = open("/Users/wangxy/Desktop/mixdata/part-000012")
# for fr in file4.readlines():
#     strArr = fr.strip().split(',')
#     Y.append(strArr[0])
#     X.append(strArr[2:])
# file4.close()

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=1000.0, random_state=0)
lr.fit(X_train_std, y_train)
res=lr.predict(X_test_std)

for i in range(0,len(res)):
    print(res[i])

n = len([i for i in range(0,len(res)) if(res[i] == y_test[i])])
poslen= len([i for i in range(0, len(res)) if (res[i] == '1')])
postrue= len([i for i in range(0, len(res)) if (res[i] == y_test[i] and y_test[i] == '1')])
print 'n=',n,'  all=',len(res), '  poslen=',poslen,'  postrue=',postrue




