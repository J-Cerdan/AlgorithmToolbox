def carFuel(travel, fuel, stopAmt, stops):
    fuelCount = 0
    reach = int(fuel)

    for i, stop in enumerate(stops):
        current = int(stop)

        if i != stopAmt-1:
            nextStop = int(stops[i+1])
        else:
            nextStop = travel

        if (reach < current):
            return -1
        elif (reach >= nextStop):
            continue
        elif (reach >= current):
            reach = current + fuel
            fuelCount += 1

        if reach >= travel:
            return fuelCount

    return -1

if __name__ == "__main__" :
    travel = int(input())
    fuel = int(input())
    stopAmt = int(input())
    stops = input().split()
    

    print(carFuel(travel, fuel, stopAmt, stops))