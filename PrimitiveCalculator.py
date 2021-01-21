# Uses python3
import sys
import math

def optimal_sequence(n):
    sequence = []

    tempSequence = []

    for number in range(n+1):
        tempSequence.append(0)

    for number in range(n+1):

        n1 = n2 = n3 = math.inf

        if number >= 2:
            
            if number%3==0:
                n3 = tempSequence[number//3]
            if number%2==0:
                n2 = tempSequence[number//2]
            
            n1 = tempSequence[number-1]

            tempSequence[number] = min(n1, n2, n3)+1

    val = n
    sequence.append(val)

    while val != 1:

        n1 = n2 = n3 = math.inf
        
        if val%3==0:
            n3 = tempSequence[val//3]
        if val%2==0:
            n2 = tempSequence[val//2]
            
        n1 = tempSequence[val-1]

        if n3 == tempSequence[val]-1:
            val = val//3
            sequence.append(val)
        elif n2 == tempSequence[val]-1:
            val = val//2
            sequence.append(val)
        else:
            val -= 1
            sequence.append(val)

    sequence.reverse()

    return sequence


        

if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
