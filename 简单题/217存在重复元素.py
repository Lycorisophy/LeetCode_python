class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        if nums == []:
            return False
        nums.sort()
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == pre:
                return True
            pre = nums[i]
        return False