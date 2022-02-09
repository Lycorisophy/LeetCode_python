def largestSumAfterKNegations(A: [int], K: int) -> int:
    A.sort()
    i = 0
    while i < K:
        if A[i] < 0:
            A[i] = -A[i]
            i += 1
        else:
            if (K - i) % 2 == 0:
                break
            if i != 0 and A[i] > A[i - 1]:
                A[i - 1] = -A[i - 1]
            else:
                A[i] = -A[i]
            break
    return sum(A)


if __name__ == '__main__':
    print(largestSumAfterKNegations(A=[4, 2, 3], K=1))
    print(largestSumAfterKNegations(A=[3, -1, 0, 2], K=3))
    print(largestSumAfterKNegations(A=[2, -3, -1, 5, -4], K=2))
