def findKthPositive(arr: [int], k: int) -> int:
    miss_i = 0
    for i, a in enumerate(arr, start=1):
        if a - i >= k:
            miss_i = i
            break
    if miss_i == 0:
        miss_i = arr.__len__()
    else:
        miss_i -= 1
    if miss_i == 0:
        return k
    miss = arr[miss_i-1]
    miss_n = miss - miss_i
    return miss + k - miss_n


if __name__ == '__main__':
    print(findKthPositive(arr = [2,3,4,7,11], k = 5))
    print(findKthPositive(arr = [1,2,3,4], k = 2))
    print(findKthPositive(arr=[3,10], k=2))

