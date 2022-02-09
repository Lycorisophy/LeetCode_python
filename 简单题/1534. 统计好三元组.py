def countGoodTriplets(arr: [int], a: int, b: int, c: int) -> int:
    n = arr.__len__()
    a += 1
    b += 1
    c += 1
    res = 0
    for i in range(n - 2):
        x = arr[i]
        for j in range(i+1, n - 1):
            y = arr[j]
            tmp = x - y
            if -a < tmp < a:
                for k in range(j+1, n):
                    z = arr[k]
                    tmp = y - z
                    if -b < tmp < b:
                        tmp = x - z
                        if -c < tmp < c:
                            res += 1
    return res


if __name__ == '__main__':
    print(countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
    print(countGoodTriplets([1, 1, 2, 2, 3], a=0, b=0, c=1))
