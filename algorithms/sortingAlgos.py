import numpy as np
import time




def createList(x):
    n = 0
    for i in range(x):
        num = np.random.randint(x)
        data.append(num)
        n+=1


def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



def quickSort(arr):

    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return quickSort(less)+equal+quickSort(greater)
    
    else:
        return arr



data = []
createList(10000)

start = time.time()
quickSort(data)
end = time.time()
qs = end - start


data = []
createList(10000)

start = time.time()
bubbleSort(data)
end = time.time()
bs = end - start


print("Quick Sort Time: " + str(qs))
print("Bubble Sort Time: " + str(bs))



