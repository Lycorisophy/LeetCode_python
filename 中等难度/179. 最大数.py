def largestNumber(nums: [int]) -> str:
    n = nums.__len__()
    for i, num in enumerate(nums):
        nums[i] = str(num)
    used = [0] * n
    res = []
    for _ in range(n):
        mf = ''
        idx = n
        for i, num in enumerate(nums):
            if used[i] == 0:
                nf = num[0]
                if nf > mf:
                    mf = nf
                    idx = i
                elif nf == mf:
                    if int(nums[idx] + num) < int(num + nums[idx]):
                        mf = nf
                        idx = i
        res.append(nums[idx])
        used[idx] = 1
    ans = ''.join(res).lstrip('0')
    return ans if ans else '0'


if __name__ == '__main__':
    print(largestNumber([0, 0]))
    print(largestNumber([3, 30, 34, 5, 9]))
    print(largestNumber([10, 2]))
    print(largestNumber([1]))
