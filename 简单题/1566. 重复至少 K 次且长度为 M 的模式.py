def containsPattern(arr: [int], m: int, k: int) -> bool:
    window_size = m * k
    n = arr.__len__()
    for i in range(n-window_size+1):
        base = arr[i:i+m]
        cnt = 0
        for j in range(1, k):
            tmp = i+j*m
            target = arr[tmp:tmp+m]
            if target != base:
                break
            else:
                cnt += 1
        if cnt == k - 1:
            return True
    return False


if __name__ == '__main__':
    print(containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
    print(containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
    print(containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))
    print(containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
    print(containsPattern(arr=[2, 2, 2, 2], m=2, k=3))
