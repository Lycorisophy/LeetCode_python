import math


def sortedSquares(nums: [int]) -> [int]:
    return sorted([num**2 for num in nums])


if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))
    print(sortedSquares([-7,-3,2,3,11]))

