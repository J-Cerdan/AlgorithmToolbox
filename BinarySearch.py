def binarySearch(arr, low, high, val):
    
    if high <= low:
        return -1
    
    mid = low + ((high-low)//2)

    if val == arr[mid]:
        return mid
    elif val < arr[mid]:
        return binarySearch(arr, low, mid, val)
    else:
        return binarySearch(arr, mid+1, high, val)


if __name__ == "__main__":

    outputArr = []
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    

    num_1 = arr_1[0]
    num_2 = arr_2[0]

    del arr_1[0]
    del arr_2[0]

    for val in arr_2:
        outputArr.append(binarySearch(arr_1, 0, num_1, val))

    print(*outputArr, sep=" ")