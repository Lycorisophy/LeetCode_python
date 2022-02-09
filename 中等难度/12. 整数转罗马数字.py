def intToRoman(num: int) -> str:
    res = ''
    levels = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    while num > 0:
        if num > 999:
            a, b = 1000, 6
        elif num > 99:
            a, b = 100, 4
        elif num > 9:
            a, b = 10, 2
        else:
            a, b = 1, 0
        x, num = divmod(num, a)
        tmp = levels[b]
        if b != 6:
            if x == 4:
                res += tmp
                res += levels[b + 1]
            elif x == 5:
                res += levels[b + 1]
            elif x == 9:
                res += tmp
                res += levels[b + 2]
            elif 5 < x < 9:
                res += levels[b + 1]
                res += (x-5) * tmp
            else:
                res += x * tmp
        else:
            res += x * tmp
    return res


if __name__ == '__main__':
    print(intToRoman(3))
    print(intToRoman(4))
    print(intToRoman(5))
    print(intToRoman(8))
    print(intToRoman(9))
    print(intToRoman(58))
    print(intToRoman(1994))
