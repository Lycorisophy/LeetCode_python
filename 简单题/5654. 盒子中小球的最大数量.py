def countBalls(lowLimit: int, highLimit: int) -> int:
    res = [0]*46
    for i in range(lowLimit, highLimit+1):
        res[sum(int(S) for S in str(i))] += 1
    return max(res)


if __name__ == '__main__':
    print(countBalls(lowLimit = 1, highLimit = 100000))