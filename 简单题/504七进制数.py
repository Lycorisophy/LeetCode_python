def convertToBase7(num: int) -> str:
    if num < 0:
        num *= -1
        c = 1
    else:
        c = 0
    res = ''
    if num < 7:
        if c == 0:
            return res+str(num)
        else:
            return res+'-'+str(num)
    while True:
        r = num % 7
        num = num//7
        res += str(r)
        if num < 7:
            res += str(num)
            if c == 1:
                res += '-'
            return res[::-1]


if __name__ == '__main__':
    print(convertToBase7(-2))
