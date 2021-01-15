import sys
import random

def fast_count_segments(starts, ends, points):

    cnt = [0] * len(points)
    runningcount = 0
    tempArr = []

    for val in starts:
        tempArr.append([val, "l"])
    
    for val in ends:
        tempArr.append([val, "r"])

    for i, val in enumerate(points):
        tempArr.append([val, "p", i])

    tempArr.sort()

    for i in range(len(tempArr)):

        obtainVal = tempArr[i][1]

        if obtainVal == "l":
            runningcount += 1
        elif obtainVal == "r":
            runningcount -= 1
        else:
            cnt[tempArr[i][2]] = runningcount

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))


    segments = data[0]
    points = data[1]

    starts = data[2:2 * segments + 2:2]
    ends   = data[3:2 * segments + 2:2]
    points = data[2 * segments + 2:]

    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts,ends,points)
    
    print(*cnt, sep=' ')
