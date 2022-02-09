import random
from copy import copy


class Solution:

    def __init__(self, nums: [int]):
        self.nums = nums
        self.o = list(nums)

    def reset(self) -> [int]:
        self.nums = self.o
        self.o = list(self.o)
        return self.nums

    def shuffle(self) -> [int]:
        n = self.nums.__len__()
        for i in range(n):
            j = random.randrange(i, n)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


if __name__ == '__main__':
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_1 = obj.reset()
    print(param_1)
    param_2 = obj.shuffle()
    print(param_2)
