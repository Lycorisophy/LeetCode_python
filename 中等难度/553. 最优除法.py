def optimalDivision(nums: [int]) -> str:
    n = nums.__len__()
    if n == 1:
        return str(nums[0])
    res = str(nums[0]) + '/'
    if n > 2:
        res += '('
    for i in range(1, n - 1):
        res += str(nums[i])
        res += '/'
    res += str(nums[n - 1])
    if n > 2:
        res += ')'
    return res
    res = str(nums[0])+'/'
    n = nums.__len__()
    if n > 2:
        res += '('
    for i in range(1, n-1):
        res += str(nums[i])
        res += '/'
    res += str(nums[n-1])
    if n > 2:
        res += ')'
    return res


if __name__ == '__main__':
    print(optimalDivision([2]))
