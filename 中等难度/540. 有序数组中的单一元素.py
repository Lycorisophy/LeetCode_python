def singleNonDuplicate(nums: [int]) -> int:
    N = len(nums)
    if N == 1:
        return nums[0]
    L, R = 0, N - 1
    while L <= R:
        M = (L+R)//2
        if M % 2 != 0:
            M += 1
        num = nums[M]
        if num == nums[M-1]:
            R = M - 1
        else:
            if M == N - 1:
                return num
            elif num == nums[M+1]:
                L = M + 1
            else:
                return num
    return nums[R]


if __name__ == '__main__':
    print(singleNonDuplicate([1, 1, 2]))
    print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
