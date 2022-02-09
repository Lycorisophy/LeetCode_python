def myAtoi(s: str) -> int:
    s = s.lstrip()
    n = s.__len__()
    if n == 0:
        return 0
    i = 0
    string = ''
    is_fushu = False
    char = s[i]
    if char == '-':
        is_fushu = True
        if n > 1 and not s[1].isnumeric():
            return 0
        if n == 1:
            return 0
    elif char == '+':
        if n > 1 and not s[1].isnumeric():
            return 0
        if n == 1:
            return 0
    elif not char.isnumeric():
        return 0
    else:
        string = char
    i += 1
    while i < n:
        char = s[i]
        if char.isnumeric():
            string += char
        else:
            break
        i += 1
    string = string.lstrip('0')
    n = string.__len__()
    if n == 0:
        return 0
    if n < 10:
        res = int(string)
        if is_fushu:
            res *= -1
    elif n > 10:
        if is_fushu:
            res = -2147483648
        else:
            res = 2147483647
    else:
        tmp1 = int(string[:5])
        if tmp1 > 21474:
            if is_fushu:
                res = -2147483648
            else:
                res = 2147483647
        elif tmp1 < 21474:
            res = int(string)
            if is_fushu:
                res *= -1
        else:
            tmp2 = int(string[5:])
            if is_fushu:
                if tmp2 >= 83648:
                    res = -2147483648
                else:
                    res = int(string)
                    res *= -1
            else:
                if tmp2 >= 83647:
                    res = 2147483647
                else:
                    res = int(string)
    return res


if __name__ == '__main__':
    print(myAtoi("000"))
    print(myAtoi(s = "4193 with words"))
    print(myAtoi("words and 987"))
    print(myAtoi("-91283472332"))
