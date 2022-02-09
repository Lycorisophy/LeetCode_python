def summaryRanges(nums: [int]) -> [str]:
    res = []
    if not nums:
        return res
    start = pre = nums[0]
    for i, data in enumerate(nums):
        if data != pre and data != (pre+1):
            if start != pre:
                res.append(str(start)+'->'+str(pre))
            else:
                res.append(str(start))
            start = data
        pre = data
    if start != pre:
        res.append(str(start) + '->' + str(pre))
    else:
        res.append(str(start))
    return res


if __name__ == '__main__':
    print(summaryRanges(nums = [0]))