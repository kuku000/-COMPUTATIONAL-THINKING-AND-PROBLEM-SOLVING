# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 23:42:33 2022

@author: KYLE
"""
from matplotlib import pylab 
import numpy as np
#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
#set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1

def getdata(filename):
    dataFile = open(filename, 'r')
    x = []
    y = []
    dataFile.readline()
    for line in dataFile:
        X ,Y =line.split(' ')
        x.append(float(X))
        y.append(float(Y))
    dataFile.close()
    return(x,y)
    
def rSquared(measured, predicted):
    estimateError = ((predicted - measured)**2).sum()
    meanOfMeasured = measured.sum()/len(measured)
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability

def fitdata2(inputfile,inputfile2):
    x,y = getdata(inputfile)
    x2,y2 = getdata(inputfile2)
    
    x = pylab.array(x)
    y = pylab.array(y)
    x2 = pylab.array(x2)
    y2 = pylab.array(y2)
    pylab.plot(y, x,'o',label ='data')
    pylab.title('odd Experiment data')
    #find linear fit
    a,b = pylab.polyfit(y,x, 1)
    fit = pylab.polyfit(y,x, 1)
    altitudes = pylab.polyval(fit,y)
    predictedx = a*pylab.array(y) + b
    #pylab.plot(y,predictedx) 
    
    degree =[2, 4, 8, 16]
    #find linear fit2
    c,d,e = pylab.polyfit(y,x,degree[0] )
    fit2 = pylab.polyfit(y,x,  degree[0])
    altitudes2 = pylab.polyval(fit2,y)
    predictedx_2 = c*pylab.array(y2)**2 + d*pylab.array(y2)    +e
    
    #find linear fit4
    f,g,h,i,j  = pylab.polyfit(y,x,degree[1] )
    fit4 = pylab.polyfit(y,x,  degree[1])
    altitudes4 = pylab.polyval(fit4,y)
    predictedx_4 = f*pylab.array(y2)**4 + g*pylab.array(y2)**3    +h*pylab.array(y2)**2 + i*pylab.array(y2) + j
    
    #find linear fit8
    p1,p2,p3,p4,p5,p6,p7,p8,p9  = pylab.polyfit(y,x,degree[2] )
    fit8 = pylab.polyfit(y,x,  degree[2])
    altitudes8 = pylab.polyval(fit8,y)
    predictedx_8 = p1*pylab.array(y2)**8 +p2*pylab.array(y2)**7 +p3*pylab.array(y2)**6     +p4*pylab.array(y2)**5 +p5*pylab.array(y2)**4 + p6*pylab.array(y2)**3    +p7*pylab.array(y2)**2 + p8*pylab.array(y2) + p9
    
    #find linear fit16
    k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17  = pylab.polyfit(y,x,degree[3])
    fit16 = pylab.polyfit(y,x,  degree[3])
    altitudes16 = pylab.polyval(fit16,y)
    predictedx_16 = k1*pylab.array(y2)**16 +k2*pylab.array(y2)**15 +k3*pylab.array(y2)**14 +k4*pylab.array(y2)**13    +k5*pylab.array(y2)**12 + k6*pylab.array(y2)**11    +k7*pylab.array(y2)**10 + k8*pylab.array(y2)**9 + k9*pylab.array(y2)**8 + k10*pylab.array(y2)**7 +     k11*pylab.array(y2)**6 + k12*pylab.array(y2)**5 + k13*pylab.array(y2)**4 + k14*pylab.array(y2)**3 +    k15*pylab.array(y2)**2 + k16*pylab.array(y2)**1 + k17
    
    
    #pylab.plot(y, altitudes,linewidth=2,color = 'orange', label = 'Fit of degree1,R2='+str(rSquared(x, altitudes).round(6))) 
    #pylab.plot(y, altitudes2,linewidth=2, color='green', label = 'Fit of degree2,R2='+str(rSquared(x, altitudes2).round(6)))
    #pylab.plot(y, altitudes4,linewidth=2, color='red', label = 'Fit of degree4,R2='+str(rSquared(x, altitudes4).round(6)))
    #pylab.plot(y, altitudes8,linewidth=2, color='purple', label = 'Fit of degree8,R2='+str(rSquared(x, altitudes8).round(6)))
    #pylab.plot(y, altitudes16,linewidth=2, color='brown', label = 'Fit of degree2,R2='+str(rSquared(x, altitudes16).round(6)))
    pylab.plot(y2,  predictedx,linewidth=2, color='orange', label = 'predict of degree2,R2='+str(rSquared(x2,predictedx).round(6)))
    pylab.plot(y2,  predictedx_2,linewidth=2, color='darkred', label = 'predict of degree2,R2='+str(rSquared(x2,predictedx_2).round(6)))
    pylab.plot(y2,  predictedx_4,linewidth=2, color='green', label = 'predict of degree4,R2='+str(rSquared(x2,predictedx_4).round(6)))
    pylab.plot(y2,  predictedx_8,linewidth=2, color='blue', label = 'predict of degree8,R2='+str(rSquared(x2,predictedx_8).round(6)))
    pylab.plot(y2,  predictedx_16,linewidth=2, color='brown', label = 'predict of degree16,R2='+str(rSquared(x2,predictedx_16).round(6)))
    pylab.legend()
    
    
fitdata2('oddExperiment.txt','TestDataSet.txt')