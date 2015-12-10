__author__ = 'wangxy'
#coding=utf-8

# map
re = map((lambda x,y: x+y),[1,2,3],[6,7,9])
print re

# filter
def func(a):
    if a > 100:
        return True
    else:
        return False

print filter(func,[10,56,101,500])

# reduce
print reduce((lambda x,y: x+y),[1,2,5,7,9])