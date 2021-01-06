def maxAd(values, aList, bList):
    totalValue = 0

    for i in range(values):
        aMax = max(aList)
        bMax = max(bList)

        totalValue += int(aMax)*int(bMax)

        aList.remove(aMax)
        bList.remove(bMax)


    return totalValue

if __name__ == "__main__":
    values = int(input())

    aList = input().split()
    bList = input().split()

    print(maxAd(values, aList, bList))