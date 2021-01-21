import math

def Change(m, coins):

    minCoins = []
    minCoins.append(0)

    for amount in range(1, m+1):

        minCoins.append(math.inf)

        for coin in coins:
            if amount >= coin:
                numCoins = minCoins[amount-coin]+1

                if numCoins < minCoins[amount]:
                    minCoins[amount] = numCoins

    return minCoins[m]

if __name__ == "__main__" :
    m = int(input())

    coins = [1, 3, 4]

    print(Change(m, coins))