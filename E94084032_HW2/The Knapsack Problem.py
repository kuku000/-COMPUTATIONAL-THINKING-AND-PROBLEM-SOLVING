# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 18:02:30 2021

@author: tiw
"""


class Item(object): 
    def __init__ (self, n, v, w): 
        self.name = n 
        self.value = v 
        self.weight = w 
    
    def getName(self): 
        return self.name
    def getValue(self): 
        return self.value 
    def getWeight(self): 
        return self.weight 
    def __str__ (self): 
        result = '<' + self.name + ', ' + str(self.value)\
        + ', ' + str(self.weight) + '>' 
        return result 
    
def value(item):
        return item.getValue() 

def weightInverse(item): 
    return 1.0/item.getWeight() 

def density(item): 
    return item.getValue()/item.getWeight() 

def greedy(items, maxWeight, keyFunction): 
    """Assumes Items a list, maxWeight >= 0, 
        keyFunction maps elements of Items to numbers""" 
    itemsCopy = sorted(items, key=keyFunction, reverse =True) 
    result = [] 
    totalValue, totalWeight = 0.0, 0.0 
    for i in range(len(itemsCopy)): 
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight: 
            result.append(itemsCopy[i]) 
            totalWeight += itemsCopy[i].getWeight() 
            totalValue += itemsCopy[i].getValue() 
    return (result, totalValue) 

def buildItems(): 
    names = ['Wine','Beer','pizza','burger','fires','coke','apple','dount'] #更改物品
    values = [85,90,30,50,90,75,90,10]                                      #各物品在那個人心中的價值
    weights = [123,154,258,354,365,150,95,195]                              #各物品的卡路里
    Items = [] 
    for i in range(len(values)): 
        Items.append(Item(names[i], values[i], weights[i])) 
    return Items 

def chooseBest(pset, maxWeight, getVal, getWeight): 
    bestVal = 0.0 
    bestSet = None 
    for items in pset: 
        itemsVal = 0.0 
        itemsWeight = 0.0 
        for item in items: 
            itemsVal += getVal(item) 
            itemsWeight += getWeight(item) 
        if itemsWeight <= maxWeight and itemsVal > bestVal: 
            bestVal = itemsVal 
            bestSet = items 
    return (bestSet, bestVal) 

def getBinaryRep(n, numDigits): 
    """Assumes n and numDigits are non-negative ints 
    Returns a str of length numDigits that is a binary representation of n""" 
    result ='' 
    while n > 0: 
        result = str(n%2) + result 
        n = n//2 
    if len(result) > numDigits:
        raise ValueError('not enough digits') 
    for i in range(numDigits - len(result)):
        result = '0' + result 
    return result
 
def genPowerset(L): 
    """Assumes L is a list Returns a list of lists that contains 
    all possible combinations of the elements of L. E.g., 
    if L is [1, 2] it will return a list with elements [], [1], [2], and [1,2].""" 
    powerset = [] 
    for i in range(0, 2**len(L)): 
        binStr = getBinaryRep(i, len(L)) 
        subset = [] 
        for j in range(len(L)): 
            if binStr[j] == '1': 
                subset.append(L[j]) 
        powerset.append(subset) 
    return powerset 

def testGreedy(items, maxWeight, keyFunction): 
    taken, val = greedy(items, maxWeight, keyFunction) 
    print('Total value of  food eaten is', val) 
    for item in taken: 
        print(' ', item) 

def testGreedys(maxWeight = 750):                                           #卡路里總數(750)
    items = buildItems() 
    print('Use greedy by value to fill your stomach', maxWeight,'Calories') 
    testGreedy(items, maxWeight, value) 
    print('\nUse greedy by weight to  fill your stomach', maxWeight,'Calories') 
    testGreedy(items, maxWeight, weightInverse) 
    print('\nUse greedy by density to fill your stomach', maxWeight,'Calories') 
    testGreedy(items, maxWeight, density) 

def testBest(maxWeight = 750) :                                             #卡路里總數(750)
    items = buildItems() 
    pset = genPowerset(items) 
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight) 
    print('\nTotal value of food eaten is', val) 
    for item in taken: 
        print(item) 
    
testGreedys()
testBest()