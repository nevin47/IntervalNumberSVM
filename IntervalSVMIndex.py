__author__ = 'nevin47'

from numpy import *
import random
import SVM
import matplotlib.pyplot as plt
import HyperIntervalNumber as HN

################## test svm #####################
## step 1: load data
print "step 1: load data..."
dataSet = []
labels = []
fileIn = open('/Users/nevin47/Desktop/Python Test/testSet.txt')
for line in fileIn.readlines():
	lineArr = line.strip().split('\t')
	newX = [float(lineArr[0]) - random.uniform(0,1),float(lineArr[0]) + random.uniform(0,1)]
	newY = [float(lineArr[1]) - random.uniform(0,1),float(lineArr[1]) + random.uniform(0,1)]
	dataSet.append([newX,newY])
	labels.append(float(lineArr[2]))
	labels.append(float(lineArr[2]))
	labels.append(float(lineArr[2]))
	labels.append(float(lineArr[2]))

NewdataSet = []
for i in dataSet:
	newI = HN.HyperIntervalNumber(i)
	out = newI.GetAllPosPoint()
	for j in out:
		NewdataSet.append(j)

dataSet2 = mat(NewdataSet)
labels = mat(labels).T
train_x = dataSet2[0:200, :]
train_y = labels[0:200, :]
test_x = dataSet2[200:400, :]
test_y = labels[200:400, :]

## step 2: training...
print "step 2: training..."
C = 0.6
toler = 0.001
maxIter = 50
svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('linear', 0))

## step 3: testing
print "step 3: testing..."
accuracy = SVM.testSVM(svmClassifier, test_x, test_y)
testResult = svmClassifier.testResult
#print len(testResult)
#print len(dataSet[8:16])
## step 4: show the result
print "step 4: show the result..."
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
SVM.showSVM(svmClassifier,dataSet[50:100])

