def largestPerimeter(nums: [int]) -> int:
    nums.sort(reverse=True)
    for i in range(len(nums)-2):
        t1, t2, t3 = nums[i:i+3]
        if t1 < t2 + t3:
            return t1 + t2 + t3
    return 0


if __name__ == '__main__':
    print(largestPerimeter([1,2,1]))
    print(largestPerimeter([3,2,3,4]))
    print(largestPerimeter([3,6,2,3]))
