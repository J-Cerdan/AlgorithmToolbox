def maxPrizes(val):
    arrValues = []

    value = val

    if val < 3: 
        print(1)
        print(val)
    else:
        for i in range(val):
            value -= i+1
            if value in arrValues or i+1 in arrValues:
                value += i+1
                continue
            else:
                arrValues.append(i+1)

            if value == 0:
                break

        print(*arrValues, sep=" ")
        




if __name__ == "__main__":
    val = int(input())

    maxPrizes(val)