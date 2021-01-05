def change(n):
    coinCount = 0

    coinCount += int(n/10)
    n %= 10

    coinCount += int(n/5)
    n %= 5

    coinCount += int(n)

    return int(coinCount)

if __name__ == "__main__":
    n = int(input())

    print(change(n))