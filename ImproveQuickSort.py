import random

def partition3(a, l, r):
    #write your code here
    sameCount = 1

    x = a[l]
    print("xvalue:" + str(x))
    j = l
    for i in range(l + 1, r + 1):

        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            sameCount += 1
            j += 1
    
    a[l], a[j] = a[j], a[l]

    print("j:"+ str(j))
    print("samecount:"+ str(sameCount))

    return j-sameCount+1, j

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    #use partition2
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)

    #use partition3
    #m1, m2 = partition3(a, l, r)
    #randomized_quick_sort(a, l, m1 - 1)
    #randomized_quick_sort(a, m2 + 1, r)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    randomized_quick_sort(arr, 0, n - 1)
    
    print(*arr, sep=' ')
