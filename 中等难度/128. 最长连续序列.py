def longestConsecutive(nums: [int]) -> int:
    longest_len = 0
    set_nums = set(nums)
    for num in set_nums:
        if num - 1 not in set_nums:
            cur_num = num
            cur_len = 1
            while cur_num + 1 in set_nums:
                cur_num += 1
                cur_len += 1
            longest_len = max(longest_len, cur_len)
    return longest_len


if __name__ == '__main__':
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
