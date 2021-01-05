def maxVal(items, maxWeight, arr, valueDict):
    valueCount = 0

    tempDict = valueDict
    tempMaxWeight = int(maxWeight)

    for i in range(items):
        if (maxWeight == 0):
            return valueCount
        
        v = max(tempDict.values())
        k = max(tempDict, key=tempDict.get)

        a = min(tempMaxWeight, int(arr[k][1]))

        valueCount += a*v
        tempMaxWeight -= a

        del tempDict[k]

    return valueCount
        


        

if __name__ == "__main__":
    initial = input()

    initial = initial.split()

    items = int(initial[0])

    maxWeight = int(initial[1])

    arr = []
    valueDict = {}

    for i in range(items):
        item = input()
        item = item.split()
        arr.append(item)
        valueDict[i] = int(item[0])/int(item[1])

    print(maxVal(items, maxWeight, arr, valueDict))