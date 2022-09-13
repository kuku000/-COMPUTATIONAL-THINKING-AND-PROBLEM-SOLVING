# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 01:21:50 2022

@author: win10
"""

import random
import pylab
#import math
import numpy as np
#import statistics
import time

start = time.time()

def variance(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)
def stdDev(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    return variance(X)**0.5

class abalone(object):
    #abalone class
    def __init__ (self,Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight,Rings): 
        self.featureVec = (Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight) 
        self.label = Rings  

    def featureDist(self, other): 
        dist = 0.0 
        for i in range(len(self.featureVec)): 
            dist += abs(self.featureVec[i] - other.featureVec[i])**2 
        return dist**0.5 

    def getLength(self): 
        return self.featureVec[0] 

    def getDiameter(self): 
        return self.featureVec[1]
    
    def getHeight(self): 
        return self.featureVec[2] 
    
    def getWhole_weight(self): 
        return self.featureVec[3] 
    
    def getShucked_weight(self): 
        return self.featureVec[4] 
    
    def getViscera_weight(self): 
        return self.featureVec[5]
    
    def getShell_weight(self): 
        return self.featureVec[6]
    
    
    
    #label <= Rings 
    def getLabel(self): 
        return self.label 

    def getFeatures(self): 
        return self.featureVec 

    def __str__ (self): 
        return str(self.getLength()) + ', ' + str(self.getDiameter())+ ', ' + str(self.getHeight())    + str(self.getWhole_weight()) + ', ' + str(self.getShucked_weight())+ ', ' + str(self.getViscera_weight())    + ', ' + str(self.getShell_weight())+ ', ' + str(self.getLabel())
    
    
    
def getBMData(filename):
    """
    
    "Diameter","Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight",
"Rings","""
    data = {}
    f = open(filename)
    next(f)
    line = f.readline() 
    data['Sex'], data['length'], data['Diameter'] = [], [], []
    data['Height'], data['Whole weight'], data['Shucked weight'] = [], [], []
    data['Viscera weight'], data['Shell weight'], data['Rings'] = [], [], []
    while line != '':
        split = line.split(',')
        data['Sex'].append(split[0])
        data['length'].append(float(split[1]))
        data['Diameter'].append(float(split[2]))
        data['Height'].append(float(split[3]))
        data['Whole weight'].append(float(split[4]))
        data['Shucked weight'].append(float(split[5])) 
        data['Viscera weight'].append(float(split[6])) 
        data['Shell weight'].append(float(split[7])) 
        data['Rings'].append(float(split[8][:-1])) #remove \n
        line = f.readline()
    f.close()
    return data



def buildabaloneExamples(fileName): 
    
    data  = getBMData(fileName)
    examples = [] 
    for i in range(len(data['Sex'])): 
        a = abalone(data['length'][i],  data['Diameter'][i],data['Height'][i],data['Whole weight'][i],data['Shucked weight'][i],data['Viscera weight'][i],data['Shell weight'][i], data['Rings'][i])
        examples.append(a)           
    return examples

def divide80_20(examples): 
    sampleIndices = random.sample(range(len(examples)), len(examples)//5) 
    trainingSet, testSet = [], [] 
    for i in range(len(examples)): 
        if i in sampleIndices: 
            testSet.append(examples[i]) 
        else: trainingSet.append(examples[i]) 
    return trainingSet, testSet

def makeHist(data, bins, title, xLabel, yLabel):
    pylab.hist(data, bins, edgecolor='black')
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    mean = sum(data)/len(data)
    std = stdDev(data)
    pylab.annotate('Mean = ' + str(round(mean, 2)) +              '\nSD = ' + str(round(std, 2)), fontsize = 20,
              xy = (0.50, 0.75), xycoords = 'axes fraction')

def findKNearest(example, exampleSet, k):
    kNearest, distances = [], []
    #Build lists containing first k examples and their distances
    for i in range(k):
        kNearest.append(exampleSet[i])
        distances.append(example.featureDist(exampleSet[i]))
    maxDist = max(distances) #Get maximum distance
    #Look at examples not yet considered
    for e in exampleSet[k:]:
        dist = example.featureDist(e)
        if dist < maxDist:
            #replace farther neighbor by this one
            maxIndex = distances.index(maxDist)
            kNearest[maxIndex] = e
            distances[maxIndex] = dist
            maxDist = max(distances)      
    return kNearest, distances

def rSquared(measured, predicted):
    estimateError = ((predicted - measured)**2).sum()
    meanOfMeasured = measured.sum()/len(measured)
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability

def cal_rmsd_numpy(coord_1, coord_2):
    #rmsd
    rmsd = np.sqrt((((coord_1 - coord_2)** 2)).mean())    ## this would be the formula
    return rmsd


def KNearestClassify(training, testSet,k):
    
    predict =[]
    real = []
    right = 0
    for e in testSet:
        real.append(e.getLabel())
        nearest, distances = findKNearest(e, training, k)
        nummatch = 0
        
        for i in range(len(nearest)):
            nummatch+=nearest[i].getLabel()
        NumMatch = nummatch/len(nearest)#avg
        predict.append(NumMatch)
        if NumMatch == e.getLabel():
            right+=1
    return predict

examples = buildabaloneExamples('abalone.txt')
trainset, testset = divide80_20(examples)

'''
#這裡是看真實分布情況
def age_distribution(examples):
    
    age = np.zeros(31)
    totalage = []
    size = 0
     
    for r in examples:
        totalage.append(r.getLabel())
        size+=1
        if r.getLabel() == 0:
            age[0]+=1
        elif r.getLabel() == 1:
            age[1]+=1
        elif r.getLabel() == 2:
            age[2]+=1
        elif r.getLabel() == 3:
            age[3]+=1
        elif r.getLabel() == 4:
            age[4]+=1
        elif r.getLabel() == 5:
            age[5]+=1
        elif r.getLabel() == 6:
            age[6]+=1
        elif r.getLabel() == 7:
            age[7]+=1
        elif r.getLabel() == 8:
            age[8]+=1
        elif r.getLabel() == 9:
            age[9]+=1
        elif r.getLabel() == 10:
            age[10]+=1
        elif r.getLabel() == 11:
            age[11]+=1
        elif r.getLabel() == 12:
            age[12]+=1
        elif r.getLabel() == 13:
            age[13]+=1
        elif r.getLabel() == 14:
            age[14]+=1
        elif r.getLabel() == 15:
            age[15]+=1
        elif r.getLabel() == 16:
            age[16]+=1
        elif r.getLabel() == 17:
            age[17]+=1
        elif r.getLabel() == 18:
            age[18]+=1
        elif r.getLabel() == 19:
            age[19]+=1
        elif r.getLabel() == 20:
            age[20]+=1
        elif r.getLabel() == 21:
            age[21]+=1
        elif r.getLabel() == 22:
            age[22]+=1
        elif r.getLabel() == 23:
            age[23]+=1
        elif r.getLabel() == 24:
            age[24]+=1
        elif r.getLabel() == 25:
            age[25]+=1
        elif r.getLabel() == 26:
            age[26]+=1
        elif r.getLabel() == 27:
            age[27]+=1
        elif r.getLabel() == 28:
            age[28]+=1
        elif r.getLabel() == 29:
            age[29]+=1
        elif r.getLabel() == 30:
            age[30]+=1
    mean=statistics.mean(totalage)
    SD =np.std(totalage)
    return age ,mean,SD
'
def Print(x,y,z):
    pylab.figure()
    y=round(y,2)
    z=round(z,2)
    x_diff=np.arange(len(x))+1
    pylab.bar(x_diff,x,label ="mean: "+str(y)+'\n'+'SD: '+str(z))
    #plt.label("mean"+str(y))
    #plt.label("SD"+str(z))
    pylab.legend()
    pylab.show()
  
age1 ,m1 ,sd1= age_distribution(buildabaloneExamples('Abalone.txt'))
Print(age1,m1,sd1)
#age2 ,m2 ,sd2= age_distribution(testset)
#Print(age2 ,m2,sd2)
'''

all_data_y = []
train_y = []
test_y = []
for e in examples:
    all_data_y.append(e.getLabel())
    
for e in trainset:
    train_y.append(e.getLabel())
for e in testset:
    test_y.append(e.getLabel())
    



makeHist(all_data_y, 20, 'All Abalone Real Rings (Age) Distribution', 'Rings', 'Number of Abalones')
pylab.show()
makeHist(test_y, 20, 'Test Set Real Rings (Age) Distribution', 'Rings', 'Number of Abalones')
pylab.show()
def abs_percent_error(abs_size,percent_size):
    abs_error = []
    percent_error = []
    Ring_vec = []
    counter = 0
    for i in range(31):
        counter += 1
        if len(abs_size[i]) == 0:
            
            #abs_error.append(0)
            #percent_error.append(0)
            continue
        Ring_vec.append(counter)
        abs_error.append(sum(abs_size[i])/len(abs_size[i]))
        percent_error.append(sum(percent_size[i])/len(percent_size[i]))
    return abs_error,percent_error,Ring_vec

def findK(training, minK, maxK, numFolds): 
    '''n-ford'''
    #Find average accuracy for range of odd values of k 
    accuracies = []
    R2 = []
    Rmsd = []
    Rmsd_min = []
    for k in range(minK, maxK + 1, 2): 
        r2 = 0
        rmsd = 0
        rmsd_min = 10000
        score = 0.0 
        for i in range(numFolds): #downsample to reduce computation time
            real =[]
            fold = random.sample(training, min(5000, len(training))) 
            examples, testSet = divide80_20(fold)
            for x in testSet:
                real.append(x.getLabel())
                
            predict = KNearestClassify(examples, testSet, k)
            right = 0
            for z in range(len(testSet)):
                if real[z] == predict[z]:
                    right+=1
            right_percent = right/len(testSet)
                    
            score += right_percent
            r2+=rSquared(np.array(real), np.array(predict))
            rmsd += cal_rmsd_numpy( np.array(real), np.array(predict))
            rmsd_temp = cal_rmsd_numpy( np.array(real), np.array(predict))
            if rmsd_min > rmsd_temp:
                rmsd_min = rmsd_temp
        accuracies.append(score/numFolds)
        R2.append(r2/numFolds)#越大越好
        Rmsd.append(rmsd/numFolds)#越小越好
        Rmsd_min.append(rmsd_min)
        
        
        
    return accuracies,R2,Rmsd,Rmsd_min

#交叉驗證 3 5 7 9
acc,r2,rmsd,rmsd_min=findK(examples,3,9,5)

count = 0

test_k = [3,5,7,9]

for i in test_k:
    
    abs_size = []
    percent_size = []
    for x in range(31):
        abs_size.append([])
        percent_size.append([])
   
    print('Pre-Training Whole Examples Evaluation with k=', i, 'is: rSquare:',r2[count],'rmsd:', rmsd[count])
    #min value for the testing time
    print('Root Mean Square Deviation(the minimum of the numFords times) for k=', i, 'is:', rmsd_min[count])
    #whole data train,trainset test
    #predict = KNearestClassify(examples, trainset, i)
    #print('Root Mean Square Deviation for k=', i, 'is:',  cal_rmsd_numpy(np.array(predict),np.array( train_y))) 
    predict = KNearestClassify(trainset, testset, i)
    print('After Trained Testing Using Test Set with k=', i, 'is: rSquare:',  round(rSquared(np.array(test_y),np.array( predict)),4), 'Rmsd:',  cal_rmsd_numpy(np.array(predict),np.array( test_y)), '\n')
    percentage_error = []
    for i in range(len(predict)):
        error = abs(predict[i] - test_y[i])
        abs_size[int(test_y[i])].append(error)
        percentage = (predict[i] - test_y[i])/test_y[i]*100
        percent_size[int(test_y[i])].append(percentage)
        percentage_error.append(percentage)
    
    
    abs_error,percent_error,Ring_vec = abs_percent_error(abs_size,percent_size)
  
    pylab.plot( Ring_vec, sorted(abs_error), label='|Errors| '+str(round(min(abs_error),2))+' to '+str(round(max(abs_error),2)))
    pylab.plot( Ring_vec,percent_error, label='% errors '+str(round(min(percent_error),2))+' to '+str(round(max(percent_error),2)))
    pylab.title('predict rings absolute and percentage error')
    pylab.xlabel('ring sizes')
    pylab.ylabel('inches and percent')
    pylab.legend()
    pylab.show()
    #畫Error圖
    makeHist(predict, 20, 'Predict Rings (Age) Absolute Errors Distribution', 'Ring Sizes', 'Number of Abalones')
    pylab.show()
    makeHist(percentage_error, 20, 'Predict Rings (Age) Percentage Errors Distribution', 'Percentage', 'Number of Abalones')
    pylab.show()    
    count+=1

end = time.time()
print("executing time",end-start)
    