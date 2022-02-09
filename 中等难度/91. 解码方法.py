def numDecodings(s: str) -> int:
    def count(S: str) -> int:
        n = S.__len__()
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if S[i - 1] != 0:
                f[i] += f[i - 1]
            if i > 1 and S[i - 2] != 0 and S[i - 2]*10 + S[i-1] <= 26:
                f[i] += f[i - 2]
        return f[n]

    res = 1
    pre = 3
    nums = []
    tmp = []
    for num in s:
        num = int(num)
        if num < 3:
            tmp.append(num)
            pre = num
        elif num < 7:
            if pre == 1 or pre == 2:
                tmp.append(num)
                nums.append(tmp)
                tmp = []
                pre = num
            else:
                if tmp:
                    nums.append(tmp)
                tmp = []
                pre = num
        else:
            if pre == 1:
                tmp.append(num)
                nums.append(tmp)
                tmp = []
                pre = num
            else:
                if tmp:
                    nums.append(tmp)
                tmp = []
                pre = num
    if tmp:
        nums.append(tmp)
    for num in nums:
        res *= count(num)
    return res


if __name__ == '__main__':
    print(numDecodings("12"))
    print(numDecodings("226"))
    print(numDecodings("0"))
    print(numDecodings("06"))
    print(numDecodings("226226"))
    print(numDecodings("2266226"))