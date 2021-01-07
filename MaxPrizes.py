def maxPrizes(val):
    setValues = set()

    values = ""

    numValues = 0

    first = 1

    value = val

    if val < 3: 
        print(1)
        print(val)
    else:
        for i in range(val):
            value -= i+1
            if value in setValues or i+1 in setValues or value == i+1:
                value += i+1
                continue
            else:
                setValues.add(i+1)
                numValues += 1

                if not first:
                    values += " "
        
                values += str(i+1)
                first = 0


            if value == 0:
                break
        print(numValues)
        print(values)
        




if __name__ == "__main__":
    val = int(input())

    maxPrizes(val)