#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
#import csv
#from numpy import loadtxt
import statistics
import pylab




#引入TXT
f = open('TemperatureofThreecities.txt','r')
text = []
for line in f:
    text.append(line.rstrip('\n').split(','))
#擷取台南的資訊
Tainan_T = text[1:10]
#存入各年分
Tainan2013 = list(map(float,Tainan_T[0]))
Tainan2014 = list(map(float,Tainan_T[1]))
Tainan2015 = list(map(float,Tainan_T[2]))
Tainan2016 = list(map(float,Tainan_T[3]))
Tainan2017 = list(map(float,Tainan_T[4]))
Tainan2018 = list(map(float,Tainan_T[5]))
Tainan2019 = list(map(float,Tainan_T[6]))
Tainan2020 = list(map(float,Tainan_T[7]))
Tainan2021 = list(map(float,Tainan_T[8]))
#建立一個array儲存台南個年份及月分資訊
Tem_array = np.zeros([9,12])
#存入個年份資訊
Tem_array[0] = Tainan2013[1:13]
Tem_array[1] = Tainan2014[1:13]
Tem_array[2] = Tainan2015[1:13]
Tem_array[3] = Tainan2016[1:13]
Tem_array[4] = Tainan2017[1:13]
Tem_array[5] = Tainan2018[1:13]
Tem_array[6] = Tainan2019[1:13]
Tem_array[7] = Tainan2020[1:13]
Tem_array[8] = Tainan2021[1:13]

#print(Tem_array)


# In[2]:


#1

plt.figure(figsize = (12, 8))
#建立X軸LIST
x_diff = [1,2,3,4,5,6,7,8,9,10,11,12]
#畫出個年份月份溫度變化
for i in range (2013,2022):
    plt.plot(x_diff,Tem_array[i - 2013],linewidth="2",label = i)
plt.xticks(range(1,13,1))
plt.title("Tainan Monthly Mean Temperature From 2013 To 2021")    
plt.legend(loc = "lower center")
plt.xlabel("Month")
plt.xlim(1,12,1)
plt.ylabel("Temperature in Degree C")
plt.show()



# In[3]:
#2

mean_list = []
#把九年各月分別平均
for i in range(0,12,1):
    mean =(Tem_array[0][i]+Tem_array[1][i]+Tem_array[2][i]+Tem_array[3][i]+Tem_array[4][i]+Tem_array[5][i]+Tem_array[6][i]+Tem_array[7][i]+Tem_array[8][i])/9
    mean_list.append(mean)
mean_year = statistics.mean(mean_list)
#九年總平均
mean_year_list = []
for i in range(12):
    mean_year_list.append(mean_year)

plt.figure(figsize = (12, 8))
#建立X軸LIST
x_diff = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x_diff,mean_list,linestyle = '-',marker = "o",color ="r")
plt.plot(x_diff,mean_list,color = "b")
plt.plot(x_diff,mean_year_list,linestyle = "--",color ="r",label = "Mean of 9 years")
#標記每一個點溫度
for i in range(12):
    plt.annotate(str(mean_list[i].round(2)),(i+1,mean_list[i]))
plt.annotate(str(mean_year.round(2)),(1,mean_year))
plt.xlim(0,12,1)
plt.xticks(range(1,13,1))
plt.title("Tainan Monthly Mean Temperature From 2013 To 2021")
plt.xlabel("Month")
plt.ylabel("Temperature in Degree C")
pylab.legend(loc ="upper right")
plt.show()


# In[136]:
#3

month_mean = []
mean_year_list_2 = []

for i in range(9):
    mean_year_list_2.append(mean_year)
#建立X軸LIST
x_diff =[2013,2014,2015,2016,2017,2018,2019,2020,2021]
#建立label的list
labels =['Mean of Jan','Mean of Feb','Mean of Mar','Mean of Apr','Mean of May','Mean of Jun','Mean of Jul','Mean of Aug','Mean of Set','Mean of Oct','Mean of Nov','Mean of Dec']
#轉至原本的矩陣
Tem_mean_T = Tem_array.transpose()
plt.figure(figsize = (12, 8))

for i in range (12):
    plt.plot(x_diff,Tem_mean_T[i],label =labels[i])
plt.plot(x_diff,mean_year_list_2,linestyle = "--",color ="r",label = "Mean of 9 years") 
plt.annotate(str(mean_year.round(2)),(2013,mean_year))
plt.title("Tainan Mean Temperature Of Month And Total Year Mean From 2013 To 2021")         
plt.legend(loc ="lower center")    
plt.xlabel("Years")
plt.ylabel("Temperature in Degree C")
plt.show()


# In[ ]:




