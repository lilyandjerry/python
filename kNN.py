#! /usr/bin/python
from numpy import *
import numpy as np
import operator

def loadDataSet(filename):
    dataList = []
    labelList = []
    fr = open(filename)
    for line in fr.readlines:
        lineArr = line.strip().split('\t')
        dataList.append(lineArr[0],lineArr[1])
        labelList.append(lineArr)
    return dataList,labelList

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1) ,reverse=True)
    return sortedClassCount[0][0]

group,labels = createDataSet()
print str(classify0([0,0],group,labels,3))