def climbStairs(n: int) -> int:
    dp = [1] * (n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]


if __name__ == '__main__':
    print(climbStairs(1))
    print(climbStairs(2))
    print(climbStairs(3))
    print(climbStairs(5))
    print(climbStairs(8))
    print(climbStairs(11))
    print(climbStairs(19))
    print(climbStairs(30))
    print(climbStairs(49))
    print(climbStairs(70))
