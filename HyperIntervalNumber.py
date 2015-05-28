__author__ = 'nevin47'

from numpy import *
import matplotlib.pyplot as plt
import IntervalNum

#DEC to BIN
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])

class HyperIntervalNumber:
    ##The hyper interval number would use 2 pemeter to describe
    def __init__(self,OriginIntervalNum):
        self.IntervalNum = mat(OriginIntervalNum)
        self.IntervalNum = self.IntervalNum.astype(float64)
        self.SampleShape = self.IntervalNum.shape

    def GetAllPosPoint(self):
        ##get all the posibility of the choice
        ResultTemp = []
        ResultFinal = []
        for i in range(2**self.SampleShape[0]):
            temp = dec2bin(i)
            alllen = self.SampleShape[0]
            resultlen = len(temp)
            Origin = []
            for j in range(alllen - resultlen):
                Origin.append(0)
            FR = Origin + list(temp)
            ResultTemp.append(FR)
        for i in ResultTemp:
            TempMiddle =[]
            for j in range(len(i)):
                TempMiddle.append(self.IntervalNum[j,i[j]])
            ResultFinal.append(TempMiddle)
        return ResultFinal

    def GetAllPosPoint2pe(self):
        if(self.SampleShape[1] != 2):
            print 'error!'
        else:
            new1 = [self.IntervalNum[0,0],self.IntervalNum[1,0]]
            new2 = [self.IntervalNum[0,0],self.IntervalNum[1,1]]
            new3 = [self.IntervalNum[0,1],self.IntervalNum[1,0]]
            new4 = [self.IntervalNum[0,1],self.IntervalNum[1,1]]
        self.PosPoint = [new1,new2,new3,new4]

    def CalMiddlePoint(self):
        TargetPoint = []
        for i in self.IntervalNum:
            Lower = i[0,0]
            Higher = i[0,1]
            Middle = (Lower + Higher)/2
            TargetPoint.append(Middle)
        return TargetPoint


# print "step 1: load data..."
# dataSet = []
# labels = []
# fileIn = open('/Users/nevin47/Desktop/Python Test/testSet.txt')
# for line in fileIn.readlines():
# 	lineArr = line.strip().split('\t')
# 	dataSet.append([float(lineArr[0]), float(lineArr[1])])
# 	labels.append(float(lineArr[2]))


##dataSet = mat()
testarray = [[1,2],[2,3],[1,2]]
a = HyperIntervalNumber(testarray)
#print a.CalMiddlePoint()
print a.GetAllPosPoint()
#print a.PosPoint
#print a.IntervalNum[0,0]