def editDistance(s1, s2):

    s1Length = len(s1)
    s2Length = len(s2)

    if s1Length == 0:
        return s2Length
    elif s2Length == 0:
        return s1Length

    #s1 = x/i, s2 = y/j
    s1List = list(s1)
    s2List = list(s2)

    grid = [ [0]*(s1Length+1) for z in range(s2Length+1)]  

    #create starting values

    for i in range(1, s1Length+1):
        grid[0][i] = i
    
    for j in range(1, s2Length+1):
        grid[j][0] = j

    for i, s1Letter in enumerate(s1List):
        for j, s2Letter in enumerate(s2List):

            #forward values
            i+=1
            j+=1
            
            if s1Letter != s2Letter:
                val1 = grid[j][i-1] #left
                val2 = grid[j-1][i] #top
                val3 = grid[j-1][i-1] #top-left corner

                grid[j][i] = min(val1, val2, val3) + 1

            else:
                grid[j][i] = grid[j-1][i-1]

            #value rollback
            i-=1
            j-=1

    return grid[s2Length][s1Length]

if __name__ == "__main__":
    print(editDistance(input(), input()))