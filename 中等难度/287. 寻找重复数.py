def findDuplicate(nums: [int]) -> int:
    slow, fast = 0, 0
    slow = nums[slow]
    fast = nums[nums[fast]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


if __name__ == '__main__':
    print(findDuplicate([1,3,4,2,2]))
    print(findDuplicate([3,1,3,4,2]))
    print(findDuplicate([1, 1]))
    print(findDuplicate([1, 1, 2]))
