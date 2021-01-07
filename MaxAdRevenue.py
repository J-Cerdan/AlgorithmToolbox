def maxAd(values, aList, bList):
    totalValue = 0

#    for i in range(values):
#        aMax = max(aList)
#        bMax = max(bList)
#
#        totalValue += int(aMax)*int(bMax)
#
#        aList.remove(aMax)
#        bList.remove(bMax)

    aList.sort()
    bList.sort()

    for i in range(len(aList)):
        totalValue += int(aList[0])*int(bList[0])
        aList.pop(0)
        bList.pop(0)



    return totalValue

if __name__ == "__main__":
    values = int(input())

    aList = input().split()
    bList = input().split()


    print(maxAd(values, aList, bList))