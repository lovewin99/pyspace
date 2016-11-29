__author__ = 'wangxy'
#coding=utf-8

# a = [2,1,3,4]
# b = '123234'
#
# print b.split("2", -1)
# print b[::-1]

# class test(object):
#     ta = 0
#     def kankan(self, nv):
#         self.ta = nv
#         return self
#
# t1 = test()
# t2 = test()
#
# print t1.kankan(1).ta
# def line_conf():
#     def line(x):
#         return 2*x+1
#     print(line(5))
#
# #if __name__ == "__main__":
# line_conf()
#
# print 'hello world'
#
# def line_conf():
#     def line(x):
#         return 2*x+1
#     return line       # return a function object
#
# my_line = line_conf()
# print(my_line(5))

# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line       # return a function object
#
# b = 5
# my_line = line_conf()
# print(my_line(5))


# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line       # return a function object
#
# b = 5
# my_line = line_conf()
# print(my_line.__closure__)
# print(my_line.__closure__[0].cell_contents)

# def line_conf(a, b):
#     def line(x):
#         return a*x + b
#     return line
#
# line1 = line_conf(1, 1)
# line2 = line_conf(4, 5)
# print(line1(5), line2(5))

# class storage(dict):
#     def __setattr__(self, key, value):
#         self[key] = value
#     def __getattr__ (self, key):
#         try:
#             print 2
#             return self[key]
#         except KeyError, k:
#             return None
#     def __delattr__ (self, key):
#         try:
#             del self[key]
#         except KeyError, k:
#             return None
#
#     def __call__ (self, key):
#         try:
#             print "1"
#             return self[key]
#         except KeyError, k:
#             return None
#
# s = storage()
# s.name = "hello" #set
# print s("name") #call
# print s["name"] #dict
# print s.name #get
# del s.name
# print s("name")
# # print s["name"]
# print s.name
# print s.__dict__.update()

# def kankan(F):
#     def kk():
#         print 'kk'
#         return F()
#     return kk()
#
# def kankan1(F):
#     print 'kk1'
#     return F()
#
# @kankan1
# def www():
#     print 'hello'
#     return
#
# www()

# from numpy import *
# a = mat([[1,2,3],[1,1,1],[1,4,5]])
# print 'a=',linalg.det(a)
#
# print 'ins = ',a.I

from numpy import *

#余弦相似度
def cosSimilar(inA,inB):
	inA=mat(inA)
	print 'inA=',inA
	inB=mat(inB)
	print 'inB=',inB
	num=float(inA*inB.T)
	print 'num=',num
	denom=linalg.norm(inA)*linalg.norm(inB)
	print 'na=',linalg.norm(inA)
	print 'nb=',linalg.norm(inB)
	print 'denom=',denom
	return 0.5+0.5*(num/denom)

print cosSimilar((1,2),(2,3))

# line={}
# line["1"]=2
# print type(line)