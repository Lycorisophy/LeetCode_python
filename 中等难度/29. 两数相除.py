def divide(dividend: int, divisor: int) -> int:
    f1, f2 = False, False
    if divisor < 0:
        divisor = -divisor
        f1 = True
    if dividend < 0:
        dividend = -dividend
        f2 = True
    f = f1 ^ f2

    if divisor > dividend:
        return 0

    lists = [divisor]
    count = [1]
    ans = 0
    while lists[-1] < dividend:
        lists.append(lists[-1] + lists[-1])
        count.append(count[-1] + count[-1])

    while dividend >= divisor:
        if lists[-1] > dividend:
            lists.pop()
            count.pop()
        else:
            dividend -= lists[-1]
            ans += count[-1]
            lists.pop()
            count.pop()

    if f:
        ans = 0 - ans
    if ans > 2147483647:
        return 2147483647
    elif ans < -2147483648:
        return -2147483648
    else:
        return ans


if __name__ == '__main__':
    print(divide(dividend=2147483647, divisor=3))
    print(divide(dividend=7, divisor=-3))
