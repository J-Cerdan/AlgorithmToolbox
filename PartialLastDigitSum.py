def PLDS(a, b):
    runningSum = 0

    if (b<=1):
        return b-1

    else:

        arr = []

        for i in range(b):
            if i <= 1:
                arr.append(i)
            else:
                arr.append((arr[i-1] + arr[i-2])%10)

            if (i>=a):
                runningSum += arr[i]

        return runningSum%10

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
    n = input().split()

    a = int(n[0])

    b = int(n[1])

    mod = 10

    pisano = pisanoPeriod(mod)

    new_a = a % pisano

    new_b = new_a + ((b - new_a) % pisano)

    print(PLDS(new_a, new_b+1))
    