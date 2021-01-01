def maxPairwiseProduct(n, array):
    val1 = 0
    val2 = 0

    arr = array.split()

    for val in arr:

        num = int(val)

        if num > val2:
            val1 = val2
            val2 = num

        elif num > val1:
            val1 = num

    return val1*val2


if __name__ == "__main__":
    n = int(input())
    array = input()

    print(maxPairwiseProduct(n, array))

