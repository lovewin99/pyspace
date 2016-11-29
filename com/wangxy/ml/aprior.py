__author__ = 'wangxy'
#coding=utf8

from numpy import *

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

# 数据去重　做字典
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])

    C1.sort()
    return map(frozenset, C1)#use frozen set so we
                            #can use it as a key in a dict

#　D数据 ck字典　minSupport最小支持度
# 返回满足要求的项和所有支持度
def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can): ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

# 对lk序列中前k个元素相同的数据合并　由apriori调用
def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
    return retList

# 一层层生成频繁项集
def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)   #原始数据
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
        print 'supK=', supK
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData

dataSet = loadDataSet()
L, suppData=apriori(dataSet)
print 'L=', L
print 'suppData=', suppData


# 生成关联规则的主函数，调用以下的两个函数　L关联规则 supportData每个频繁项集的支持度字典
def generateRules(L, supportData, minConf=0.7):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]  # 取大于２的每个关联规则的去重元素　[frozenset([1]), frozenset([3])]
            print 'H1=', H1
            if (i > 1):
                print '11111111'
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                # 如果频繁项只有两个元素，那么直接计算可信度
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

# 计算可信度
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf:
            print freqSet-conseq,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

# 从最初的项集中生成更多的关联规则　freqset 一个长度大于２的频繁项　H：去重元素　[frozenset([1]), frozenset([3])]　supportData所有频繁项的支持度　brl即为返回值
def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)

rules = generateRules(L, suppData, minConf=0.7)
print 'rules=', rules