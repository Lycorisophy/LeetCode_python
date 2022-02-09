def numMovesStonesII(stones: [int]) -> [int]:
    stones.sort()
    n = len(stones)
    inter_space = stones[-1] - stones[0] + 1 - n

    max_ = inter_space - min(stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1)
    # 主要卡第一步，因为必须交叉着进行  以后的步骤，都可以想办法，每次范围只缩小1
    min_ = max_
    R = 0
    for L in range(n):
        while R + 1 < n and stones[R + 1] - stones[L] + 1 <= n:  # 维护一个长度为n的窗口
            R += 1
        cost = n - (R - L + 1)  # 窗口内的空格的个数

        if R - L + 1 == n - 1 and stones[R] - stones[L] + 1 == n - 1:  # 示例2： 3 4 5 6 10，最少操作数不是1，是2
            cost = 2

        min_ = min(min_, cost)
    return [max_, min_]


if __name__ == '__main__':
    print(numMovesStonesII([7, 4, 9]))
    print(numMovesStonesII([6, 5, 4, 3, 10]))
    print(numMovesStonesII([100, 101, 104, 102, 103]))
