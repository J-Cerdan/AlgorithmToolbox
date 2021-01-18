import sys
import math
import random

def minimum_distance(x, y, n):
    #write your code here
    
    if n < 4:
        minVal = math.sqrt(math.pow((x[0][0]-x[1][0]), 2)+math.pow((x[0][1]-x[1][1]), 2))

        for i in range(n):
            for j in range(n):
                if i != j:
                    calVal = math.sqrt(math.pow((x[i][0]-x[j][0]), 2)+math.pow((x[i][1]-x[j][1]), 2))

                    if calVal < minVal:
                        minVal = calVal
        
        return minVal

    midIndex = n//2

    Qx = x[:midIndex]
    Rx = x[midIndex:]

    leftMinVal = minimum_distance(Qx, y, midIndex)
    rightMinVal = minimum_distance(Rx, y, n-midIndex)

    minVal = min(leftMinVal, rightMinVal)

    if minVal == 0:
        return minVal

    return calculateMiddle(x, y, minVal)

def calculateMiddle(x, y, minVal):

    midIndex = len(x)//2
    midX = x[midIndex][0]
    
    for val in y:
        if (val[0] < (midX-minVal)) or (val[0] > (midX+minVal)):
            y.remove(val)

    for i in range(len(y)-1):
        for j in range(min(7, len(y)-i)):
            if i != j:
                calVal = math.sqrt(math.pow((y[i][0]-y[i+j][0]), 2)+math.pow((y[i][1]-y[i+j][1]), 2))

                if calVal < minVal:
                    minVal = calVal

    return minVal


def randomized_quick_sort(a, l, r, coordinate):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    #use partition3
    m1, m2 = partition3(a, l, r, coordinate)
    randomized_quick_sort(a, l, m1 - 1, coordinate)
    randomized_quick_sort(a, m2 + 1, r, coordinate)

def partition3(a, l, r, coordinate):
    #write your code here
    x = a[l][coordinate]
    j = i = l
    k = r

    while i <= k :
        if a[i][coordinate] < x:
            a[i], a[j] = a[j], a[i]
            j += 1

        elif a[i][coordinate] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
            i -= 1 
        i += 1  
         
    return j, k

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    pointsXSorted = []
    pointsYSorted = []

    for i in range(n):
        pointsXSorted.append([x[i], y[i]])
        pointsYSorted.append([x[i], y[i]])

    randomized_quick_sort(pointsXSorted, 0, len(pointsXSorted)-1, 0)
    randomized_quick_sort(pointsYSorted, 0, len(pointsYSorted)-1, 1)

    midX = pointsXSorted[n//2]

    print("{0:.9f}".format(minimum_distance(pointsXSorted, pointsYSorted, n)))
