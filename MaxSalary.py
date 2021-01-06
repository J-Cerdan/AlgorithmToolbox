def maxSalary(n, numbers):

    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            value1 = int(numbers[j]+numbers[j+1])
            value2 = int(numbers[j+1]+numbers[j])

            if value2 > value1:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(*numbers, sep="")



if __name__ == "__main__":
    n = int(input())
    numbers = input().split()

    maxSalary(n, numbers)

