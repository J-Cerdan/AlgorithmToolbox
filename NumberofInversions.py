def get_number_of_inversions(a, length):

    number_of_inversions = 0

    if length <= 1:
        return number_of_inversions

    avg = length // 2
    A = a[:avg]
    B = a[avg:]
    number_of_inversions += get_number_of_inversions(A, avg)
    number_of_inversions += get_number_of_inversions(B, length-avg)

    #write your code here
    i = 0


    while A and B:

        if A[0] <= B[0]:
            a[i] = A.pop(0)
        else:
            a[i] = B.pop(0)
            number_of_inversions += len(A)
        i+=1

    while A:
        a[i] = A.pop(0)
        i+=1

    while B:
        a[i] = B.pop(0)
        i+=1

    return number_of_inversions


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    print(get_number_of_inversions(arr, n))