#!/usr/bin/env python
# coding: utf-8

# In[32]:


from matplotlib import pylab 


# In[44]:


'''第一題至第三題'''

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


# In[47]:


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
def fitdata(inputfile):
    x,y = getdata(inputfile)
    x = pylab.array(x)
    y = pylab.array(y)
    pylab.plot(y, x,'o',linewidth=2,label ='data')
    pylab.title('odd Experiment data')
    #find linear fit 
    a,b = pylab.polyfit(y,x, 1)
    fit = pylab.polyfit(y,x, 1)
    altitudes = pylab.polyval(fit,y)
    predictedx = a*pylab.array(y) + b
    pylab.plot(y,predictedx)
   # pylab.plot(y, altitudes, color='orange', label = 'Fit of degree1,LSE='+str(LSE(x, altitudes).round(6)))
   # pylab.plot(y, altitudes, 'r', label = 'Fit of degree1,R2='+str(rSquared(x, altitudes).round(6))) 
    # find quadratic fit
    c,d,e = pylab.polyfit(y,x, 2)
    fit2 = pylab.polyfit(y,x, 2)
    altitudes2 = pylab.polyval(fit2,y)
    predictedx_2 = c*pylab.array(y)**2 + d*pylab.array(y)    +e
    pylab.plot(y,predictedx_2,linewidth=2)
    pylab.plot(y, altitudes, color='orange',linewidth=2, label = 'Fit of degree1,LSE='+str(LSE(x, altitudes).round(6)))
    pylab.plot(y, altitudes2, color='green',linewidth=2, label = 'Fit of degree1,LSE='+str(LSE(x, altitudes2).round(6)))
    pylab.plot(y, altitudes, 'r',linewidth=2, label = 'Fit of degree1,R2='+str(rSquared(x, altitudes).round(6))) 
    pylab.plot(y, altitudes2, color='purple',linewidth=2, label = 'Fit of degree2,R2='+str(rSquared(x, altitudes2).round(6)))
    pylab.legend()
    
    
def rSquared(measured, predicted):
    estimateError = ((predicted - measured)**2).sum()
    meanOfMeasured = measured.sum()/len(measured)
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability    

def LSE(measured, predicted):
    estimateError = ((predicted - measured)**2).sum()/len(predicted)
    return estimateError
    
    
        
    
    
    


fitdata('oddExperiment.txt')
#fitdata('TestDataSet.txt')


# In[ ]:





# In[ ]:




