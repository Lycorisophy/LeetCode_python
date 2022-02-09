def majorityElement(nums: [int]) -> int:
    # Boyer - Moore投票算法 摩尔投票
    n = len(nums)
    x, cnt = -1, 0  # x 是当前队伍，cnt是当前队伍剩余人数
    for num in nums:
        if not cnt:  # 前面的都挂了
            x = num
        if x == num:
            cnt += 1  # 相同的归队
        else:
            cnt -= 1  # 不同的同归于尽
    return x if cnt and nums.count(x) > n // 2 else -1  # x是最后的队伍


if __name__ == '__main__':
    print(majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5]))
    print(majorityElement([3, 2]))
    print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(majorityElement([1]))
