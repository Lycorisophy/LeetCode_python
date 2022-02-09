def rotatedDigits(N: int) -> int:
    n = 0
    res = [0, 316, 633, 975, 975, 976, 1319, 1661, 1661, 1978, 2320]
    b = N // 1000
    for i in range(b*1000+1, N+1):
        can_rotated = False
        for s in str(i):
            if s not in ['0', '1', '8', '2', '5', '6', '9']:
                can_rotated = False
                break
            elif s in ['2', '5', '6', '9']:
                can_rotated = True
        if can_rotated:
            n += 1
    return n + res[b]


if __name__ == '__main__':
    print(rotatedDigits(2))

