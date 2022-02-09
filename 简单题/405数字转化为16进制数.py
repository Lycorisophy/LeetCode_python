def toHex(num: int) -> str:
    hexs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if num > 0:
        res = []
        r = ''
        while num > 15:
            div = num // 16
            mod = num - div * 16
            res += hexs[mod]
            num = div
        res += hexs[num]
        for i in range(len(res)):
            r += res[-i-1]
        return r
    elif num == 0:
        return '0'
    else:
        num = 4294967296 + num
        res = []
        r = ''
        while num > 15:
            div = num // 16
            mod = num - div * 16
            res += hexs[mod]
            num = div
        res += hexs[num]
        for i in range(len(res)):
            r += res[-i - 1]
        return r


if __name__ == '__main__':
    print(toHex(num=-1))