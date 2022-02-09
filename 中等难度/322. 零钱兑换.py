import functools


def coinChange(coins: [int], amount: int) -> int:
    @functools.lru_cache(amount)
    def dp(rem: int) -> int:
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        res = []
        for coin in coins:
            ret = dp(rem-coin)
            if ret != -1:
                res.append(ret)
        return min(res)+1 if res else -1

    if amount < 1:
        return 0
    return dp(amount)


if __name__ == '__main__':
    print(coinChange(coins=[1, 2, 5], amount=11))
    print(coinChange(coins=[2], amount=3))
    print(coinChange(coins=[1], amount=0))
    print(coinChange(coins=[1], amount=1))
    print(coinChange(coins=[1], amount=2))
