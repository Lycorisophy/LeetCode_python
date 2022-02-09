def countPrimeSetBits(L: int, R: int) -> int:
    ps = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]
    cnt = 0
    for i in range(L, R + 1):
        if ps[bin(i).count('1')] == 1:
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(countPrimeSetBits(1, 1000))
