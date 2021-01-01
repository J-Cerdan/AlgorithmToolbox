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


if __name__ == "__main__":
    n = int(input())

    print(countFibonacci(n+1))