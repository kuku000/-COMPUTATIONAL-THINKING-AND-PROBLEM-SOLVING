import time
import random
import numpy as np
W=20
weights=[0,3, 2, 7, 19, 3, 10, 1, 14] 
values=[0,8, 8, 1, 18, 14, 4, 16, 1]
n=8










def bigTest(numItems, capacity): 
    global values, weights    
  
    print(values[1:])
    print(weights[1:])
    items= np.zeros((numItems+1, capacity+1), dtype=int)  #create a numItems*maxWeight array with elements initialized to 0

    for i in range(1, numItems+1):    # Cponsider every objects
        for j in range(capacity+1): # Condsider every object's weight
            if weights[i] > j : # wi>W the new item is more than the current weight limit 
                items[i][j] = items[i-1][j]
            else :                # wi<=W ????
                items[i][j] = max(items[i-1][j], items[i-1][j-weights[i]] + values[i])

    print(items)    
    return items[numItems][capacity]



def maxValue(i, j):
    """Define function m to get the maximum value 
    under the condition: use first numItems items, total weight limit is capacity"""
    if i == 0 or j <= 0 :
        items[i][j] = 0
        return items[i][j]

    if (items[i-1][j] == -1) :     # m[i-1, j] has not been calculated, we have to call function m
        items[i-1][j] = maxValue(i-1, j)

    if weights[i] > j :                      # item cannot fit in the bag
        items[i][j] = items[i-1][j]
    else: 
        if (items[i-1][j-weights[i]] == -1) :     # m[i-1,j-weights[i]] has not been calculated, we have to call function m
            items[i-1][j-weights[i]] = maxValue(i-1, j-weights[i])
        items[i][j] = max(items[i-1][j], items[i-1][j-weights[i]] + values[i])
    return items[i][j]

""" /**
 * Returns the indices of the items of the optimal knapsack.
 * i: We can include items 1 through i in the knapsack
 * j: maximum weight of the knapsack
 */"""
def knapsack(i, j):
    if i == 0 :
        return {}
    if items[i][j] > items[i-1][ j]:
        return {i}.union(knapsack(i-1, j-weights[i]))
    else:
        return knapsack( i-1, j)
    
def bigTest2(numItems, capacity):
#    values, weights = buildManyItems(numItems, 20, 20) 
    global items
    items = np.full((numItems+1, capacity+1), -1, dtype=int)  #create a numItems*maxWeight array with elements initialized to 0
#    print(items)
    maxValue(numItems, capacity )
    print(values[1:])
    print(weights[1:])
    print(items)    
    print(knapsack(numItems, capacity))
    return items[numItems][capacity]  

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
    
def maxVal(toConsider, avail): 
    """Assumes toConsider a list of items, avail a weight 
    Returns a tuple of the total value of a solution to the 0/1 knapsack problem 
    and the items of that solution""" 
    if toConsider == [] or avail == 0:
        result = (0, ()) 
    elif toConsider[0].getWeight() > avail: 
        #Explore right branch only 
        result = maxVal(toConsider[1:], avail) 
    else: 
        nextltem = toConsider[0] 
        #Explore left branch 
        withVal, withToTake = maxVal(toConsider[1:], avail - nextltem.getWeight())
        withVal += nextltem.getValue()
        #Explore right branch 
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail) 
        #Choose better branch 
        if withVal > withoutVal: 
            result = (withVal, withToTake + (nextltem,)) 
        else: 
            result = (withoutVal, withoutToTake) 
    return result 


start=time.time()
print(bigTest(n, W))
end=time.time()
print('Execution time of nonrecursive version is:', end-start)

start=time.time()
print(bigTest2(n, W))
end=time.time()
print('Execution time of recursive version is:', end-start)





start=time.time()

end=time.time()

