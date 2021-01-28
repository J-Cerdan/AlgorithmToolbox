def MaxGold(maxWeight, amount, values):

    grid = [[ 0 for z in range(maxWeight+1)] for y in range(amount+1)]

    for i in range(1, amount+1):
        for w in range(1, maxWeight+1):
            grid[i][w] = grid[i-1][w]

            weight = values[i-1]

            if weight <= w:
                val = grid[i-1][w-weight]+weight
                if grid[i][w] < val:
                    grid[i][w] = val

    return grid[amount][maxWeight]
    

if __name__ == "__main__":
    n = list(map(int, input().split()))

    maxWeight = n[0]
    amount = n[1]

    values = list(map(int, input().split()))

    print(MaxGold(maxWeight, amount, values))