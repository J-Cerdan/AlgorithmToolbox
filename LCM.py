def calcGCD(val1, val2):

    if (val2 == 0):
        return val1
    else:

        temp = val2

        val2 = val1 - (int(val1/val2)*val2)

        val1 = temp

        return int(calcGCD(val1, val2))

def LCM(a, b):

    #formula from artofproblemsolving.com

    return (a*b) / calcGCD(a, b)


if __name__ == "__main__":
    n = input().split()
    
    a, b = int(n[0]), int(n[1])

    if b > a:
        a, b = b, a

    print(int(LCM(a, b)))




