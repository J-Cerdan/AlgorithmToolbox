def majorityElement(n, arr):
    arr.sort()

    valueDict = {}

    for val in arr:

        #returns amount or none
        checkVal = valueDict.get(val)

        if checkVal == None:
            valueDict[val] = 1
        elif checkVal != None:
            valueDict[val] = checkVal + 1

    majority = max(valueDict.values())

    if majority > n/2:
        return 1
    else:
        return 0
            

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    print(majorityElement(n, arr))