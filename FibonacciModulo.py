def countFibonacci(n):

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
    n = input().split()

    val = int(n[0])

    mod = int(n[1])

    pisano = pisanoPeriod(mod)

    new_val = val % pisano

    print(countFibonacci(new_val+1)%mod)