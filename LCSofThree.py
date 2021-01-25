def LCS(n1, n2, n3, n1Length, n2Length, n3Length):

    if (n1Length == 0 or n2Length == 0 or n3Length == 0):
        return 0

    cube = [[[0 for k in range(n1Length+1)] for j in range(n2Length+1)] for i in range(n3Length+1)]


    for i, n1Number in enumerate(n1):
        for j, n2Number in enumerate(n2):
            for k, n3Number in enumerate(n3):

                #forward values
                i+=1
                j+=1
                k+=1

                val1 = cube[k-1][j][i] #left
                val4 = cube[k][j][i-1]
                val2 = cube[k][j-1][i] #top
                val3 = cube[k-1][j-1][i-1] #top-left corner

                if n1Number == n2Number == n3Number:
                    cube[k][j][i] = val3 + 1
                
                else:
                    cube[k][j][i] = max(val1,val2, val4)

                #value rollback
                i-=1
                j-=1
                k-=1

    
    return cube[n3Length][n2Length][n1Length]

if __name__ == "__main__":
    n1Length = int(input())
    n1 = list(map(int, input().split()))
    n2Length = int(input())
    n2 = list(map(int, input().split()))
    n3Length = int(input())
    n3 = list(map(int, input().split()))

    print(LCS(n1, n2, n3, n1Length, n2Length, n3Length))