__author__ = 'wangxy'
#coding=utf-8

# range
S = 'abcdefghijk'
for i in range(0,len(S),2):
    print S[i]
# enumerate
S1 = 'abcdefghijk'
for (index,char) in enumerate(S1):
    print index
    print char

# zip
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)

ta = [1,2,3]
tb = [9,8,7]

# cluster
zipped = zip(ta,tb)
print(zipped)

# decompose
na, nb = zip(*zipped)
print(na, nb)

# 循环对象
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

for i in gen():
    print i