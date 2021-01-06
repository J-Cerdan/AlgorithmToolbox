def collectSignatures(values, arr):

    tempArr = arr

    coordinate = []


    while len(tempArr) != 0:
        comparingValue = tempArr[0]
        capturedNum = None
        tempArr.remove(comparingValue)

        for i in range(int(comparingValue[1]), int(comparingValue[0])-1, -1):
            for ranges in tempArr:

                if i <= int(ranges[1]) and i >= int(ranges[0]) and capturedNum == None:
                    tempArr.remove(ranges)
                    coordinate.append(i)
                    capturedNum = i
                elif capturedNum != None and capturedNum <= int(ranges[1]) and capturedNum >= int(ranges[0]):
                    tempArr.remove(ranges)
                    

    coordinate.sort()
    
    print(len(coordinate))
    print(*coordinate, sep=" ")


if __name__ == "__main__":
    values = int(input())

    arr = []

    for i in range(values):
        arr.append(input().split())

    collectSignatures(values, arr)