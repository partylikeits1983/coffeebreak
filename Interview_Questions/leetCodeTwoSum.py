from random import random
from random import randint

def twoSum(nums, target):
    foundSolution = False
    i = 0
    solutionList = []

    while i < len(nums) and not foundSolution:
        j = i + 1
        while j < len(nums) and not foundSolution:
            if nums[i] + nums [j] == target:
                foundSolution = True
                solutionList.append(i)
                solutionList.append(j)

            j += 1
        i += 1


    print(solutionList)
    return solutionList


def randomArray(n):
    nums = []

    for _ in range(n):
        value = randint(0, 10)
        nums.append(value)

    target = randint(0,20)
    print(nums)
    print(target)
    twoSum(nums, target)

randomArray(int(input()))

#nums = [1,2,4,6,2,8,3,2,4,5,3,5,6,7,8,1,0,1,4,5,2,3,4,9,20]
#target = 29

#twoSum(nums,target)
