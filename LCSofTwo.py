def LCS(n1, n2, n1Length, n2Length):

    if n1Length == 0 or n2Length == 0:
        return min(n1Length, n2Length)

    grid = [ [0]*(n1Length+1) for z in range(n2Length+1)]

    for i, n1Number in enumerate(n1):
        for j, n2Number in enumerate(n2):

            #forward values
            i+=1
            j+=1

            val1 = grid[j][i-1] #left
            val2 = grid[j-1][i] #top
            val3 = grid[j-1][i-1] #top-left corner

            if n1Number == n2Number:
                grid[j][i] = val3 + 1
            
            else:
                grid[j][i] = max(val1,val2)

            #value rollback
            i-=1
            j-=1

 
    return grid[n2Length][n1Length]

    

if __name__ == "__main__":
    n1Length = int(input())
    n1 = list(map(int, input().split()))
    n2Length = int(input())
    n2 = list(map(int, input().split()))

    print(LCS(n1, n2, n1Length, n2Length))