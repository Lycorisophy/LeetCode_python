def maxUncrossedLines(nums1: [int], nums2: [int]) -> int:
    n1, n2 = len(nums1), len(nums2)
    dp = [[0 for _ in range(n2)] for _ in range(n1)]
    f1, f2 = nums1[0], nums2[0]
    if f1 == f2:
        dp[0][0] = 1
    for i in range(1, n2):
        dp[0][i] = dp[0][i-1]
        if nums2[i] == f1:
            dp[0][i] = 1
    for i in range(1, n1):
        dp[i][0] = dp[i-1][0]
        if nums1[i] == f2:
            dp[i][0] = 1
    for i in range(1, n1):
        for j in range(1, n2):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


if __name__ == '__main__':
    print(maxUncrossedLines([3,2],[2,2,2,3]))
    print(maxUncrossedLines(nums1=[1, 3, 7, 1, 7, 5], nums2=[1, 9, 2, 5, 1]))
    print(maxUncrossedLines(nums1=[1, 4, 2], nums2=[1, 2, 4]))
    print(maxUncrossedLines(nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]))
