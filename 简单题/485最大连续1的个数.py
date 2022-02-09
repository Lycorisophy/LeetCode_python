def findMaxConsecutiveOnes(nums: [int]) -> int:
    nums.append(0)
    m, c = 0, 0
    for n in nums:
        if n == 1:
            c += 1
        else:
            m = max(m, c)
            c = 0
    return m


if __name__ == '__main__':
    print(findMaxConsecutiveOnes([0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,1]))