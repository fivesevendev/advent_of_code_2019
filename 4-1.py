#AOC-2019-4-1


import timeit, sys, time


testData = []

data = []


def numFind(n):
    count = 0
    for x in range(n[0], n[1]):
        if increase(x):
            if double(x):
                count += 1
    return count

def increase(n):
    nums = list(str(n))
    for x in range(1, len(nums)):
        if int(nums[x]) < int(nums[x - 1]):
            return False
    return True

def double(n):
    nums = list(str(n))
    for x in range(1, len(nums)):
        if nums[x] == nums[x - 1]:
            return True
    return False


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = (234208, 765869)
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")