import random


class Solution:

    def __init__(self, nums: [int]):
        nums.sort()
        self.nums = nums
        self.len = nums.__len__()

    def pick(self, target: int) -> int:
        L, R = 0, self.len - 1
        res = []
        while L <= R:
            m = L + (R - L) // 2
            if self.nums[m] > target:
                R = m - 1
            elif self.nums[m] < target:
                L = m + 1
            elif self.nums[m] == target:
                res.append(m)
                L = m - 1
                R = m + 1
                while L >= 0 and self.nums[L] == target:
                   res.append(L)
                   L -= 1
                while R < self.len and self.nums[R] == target:
                   res.append(R)
                   R += 1
                break
        x = random.randint(0, len(res)-1)
        return res[x]


if __name__ == '__main__':
    s1 = Solution([1,2,3,3,3])
    print(s1.pick(3))
    print(s1.pick(1))
    print(s1.pick(2))
