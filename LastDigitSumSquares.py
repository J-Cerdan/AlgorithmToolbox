def LDSS(n):

    if (n<=1):
        return n-1

    else:

        arr = []

        for i in range(n):
            if i <= 1:
                arr.append(i)
            else:
                arr.append(arr[i-1] + arr[i-2])

        return arr.pop()

def pisanoPeriod(m):
    a = 0
    b = 1
    c = a+b

    for i in range (m*m):

        c = (a+b)%m
        a, b = b, c
        
        if (a == 0 and b == 1):
            return int(i + 1)

if __name__ == "__main__":
    n = int(input())

    modulo = 10

    pisano = pisanoPeriod(modulo)

    new_val = n % pisano

    value_1 = LDSS(new_val)%modulo

    value_2 = LDSS(new_val+1)%modulo

    area = value_2*(value_1+value_2)

    print(area%modulo)
    