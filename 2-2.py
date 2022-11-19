#AOC-2019-2-2


import timeit, sys, time


testData = [1,1,1,4,99,5,6,0,99]

data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0]


def nounVerb():
    for noun in range(0, 100):
        for verb in range(0, 100):
            tempData = data[::]
            tempData[1] = noun
            tempData[2] = verb
            if numFind(tempData) == 19690720:
                return 100 * noun + verb

def numFind(n):
    for i in range(0, len(n), 4):
        if n[i] == 99:
            break
        a = n[n[i + 1]]
        b = n[n[i + 2]]
        if n[i] == 1:
            output = a + b
        elif n[i] == 2:
            output = a * b
        n[n[i + 3]] = output
    return n[0]


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    print("Result:", nounVerb())
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")