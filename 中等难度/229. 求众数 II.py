def majorityElement(nums: [int]) -> [int]:
    n = nums.__len__()
    m = n // 3 + 1
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    res = []
    for k, v in dic.items():
        if v >= m:
            res.append(k)
    return res


if __name__ == '__main__':
    print(majorityElement([3,2,3]))
    print(majorityElement([1]))
    print(majorityElement([1,1,1,3,3,2,2,2]))
    print(majorityElement([1, 2, 3]))
