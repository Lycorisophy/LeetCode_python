def findDisappearedNumbers(nums: [int]) -> [int]:
    res = [0]*len(nums)
    a = []
    for num in nums:
        res[num-1] += 1
    for i, re in enumerate(res):
        if re == 0:
            a.append(i+1)
    return a


if __name__ == '__main__':
    print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))