from cffi.backend_ctypes import xrange


def largestSumOfAverages(nums: [int], k: int) -> float:
    P = [0]
    for x in nums:
        P.append(P[-1] + x)

    def average(i, j):
        return (P[j] - P[i]) / float(j - i)

    N = len(nums)
    dp = [average(i, N) for i in xrange(N)]
    for k in xrange(k - 1):
        for i in xrange(N):
            for j in xrange(i + 1, N):
                dp[i] = max(dp[i], average(i, j) + dp[j])

    return dp[0]



if __name__ == '__main__':
    print(largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4))
    print(largestSumOfAverages([9, 1, 2, 3, 9], 2))
    print(largestSumOfAverages([9, 1, 2, 3, 9], 1))
    print(largestSumOfAverages([9, 1, 2, 3, 9], 4))
    print(largestSumOfAverages([9, 1, 2, 3, 9], 5))
    print(largestSumOfAverages([9, 1, 2, 3, 9, 9, 1, 2, 3, 9], 3))
