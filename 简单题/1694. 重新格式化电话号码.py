def reformatNumber(number: str) -> str:
    nums = []
    n = 0
    for num in number:
        if num != '-' and num != ' ':
            nums.append(num)
            n += 1
    a, b = divmod(n, 3)
    res = ''
    cnt = 0
    if b == 1:
        for i in range(n-4):
            res += nums[i]
            cnt += 1
            if cnt == 3:
                cnt = 0
                res += '-'
        res += nums[n - 4]
        res += nums[n - 3]
        res += '-'
        res += nums[n - 2]
        res += nums[n - 1]
        return res
    for i in range(n):
        res += nums[i]
        cnt += 1
        if cnt == 3:
            cnt = 0
            if i != n-1:
                res += '-'
    return res


if __name__ == '__main__':
    print(reformatNumber("1-23-45 6"))
    print(reformatNumber("123 4-567"))
    print(reformatNumber("123 4-5678"))
    print(reformatNumber("123 4-5678"))
