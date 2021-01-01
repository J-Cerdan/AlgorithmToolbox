def calcGCD(val1, val2):

    if (val2 == 0):
        return val1
    else:

        temp = val2

        val2 = val1 - (int(val1/val2)*val2)

        val1 = temp

        return calcGCD(val1, val2)
   
    

if __name__ == "__main__":
    n = input().split()

    val1 = int(n[0])
    val2 = int(n[1])

    #Make val1 higest value
    if (val2 > val1):
        val1, val2 = val2, val1

    print(calcGCD(val1, val2))