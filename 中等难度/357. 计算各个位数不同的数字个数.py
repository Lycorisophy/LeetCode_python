def countNumbersWithUniqueDigits(n: int) -> int:
    if n == 0:
        return 1
    dp = [1] * (n + 1)
    dp[1] = 10

    def get_cnt(x: int) -> int:
        if x > 9:
            return 0
        num = 9
        res = 9
        while x > 1:
            res *= num
            x -= 1
            num -= 1
        return res

    for i in range(2, n+1):
        cnt = get_cnt(i)
        dp[i] = dp[i-1] + cnt
    return dp


if __name__ == '__main__':
    print(countNumbersWithUniqueDigits(20))
