# 给定一个长度为 n 的 非空 整数数组，每次操作将会使 n - 1 个元素增加 1。找出让数组所有元素相等的最小操作次数。
def minMoves(nums: [int]) -> int:
    return sum(nums)-min(nums)*len(nums)


if __name__ == '__main__':
    print(minMoves(nums=[1, 2, 3]))
