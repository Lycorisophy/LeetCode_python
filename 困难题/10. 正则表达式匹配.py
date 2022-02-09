def isMatch(s: str, p: str) -> bool:
    a, b = [], []
    if s == '':
        a = []
        cnt = 0
    else:
        pre = s[0]
        cnt = 0
        for char in s:
            if char == pre:
                cnt += 1
            else:
                a.append([pre, cnt])
                cnt = 1
                pre = char
        if cnt != 0:
            a.append([pre, cnt])
            cnt = 0
    pre = ''
    for char in p:
        if char == pre or pre == '':
            cnt += 1
            pre = char
        else:
            if char == '*':
                b.append([pre, -1])
                cnt = 0
                pre = ''
            else:
                b.append([pre, cnt])
                cnt = 1
                pre = char
    if cnt != 0 and pre != '':
        b.append([pre, cnt])
    i, j = 0, 0
    n1, n2 = a.__len__(), b.__len__()
    while i < n1 and j < n2:
        a1, a2 = a[i]
        b1, b2 = b[j]
        if a1 == b1:
            if b2 == -1:
                i += 1
            elif a2 < b2:
                return False
            elif a2 == b2:
                i += 1
                j += 1
            else:
                a[i][1] -= b2
                j += 1
        elif b1 == '.':
            if b2 == -1:
                return True
            else:
                if a2 > 1:
                    a[i][1] -= b2
                    j += 1
                else:
                    i += 1
                    j += 1
        else:
            if b2 == -1:
                j += 1
            else:
                return False
    if i == n1 and j == n2:
        return True
    return False



if __name__ == '__main__':
    print(isMatch(s="ab", p=".*"))
    print(isMatch(s="aab", p="c*a*b"))
    print(isMatch(s="mississippi", p="mis*is*p*."))
    print(isMatch(s="a", p="a"))
    print(isMatch(s="aa", p="a*"))
    print(isMatch(s="aa", p="a*."))
    print(isMatch(s="aa", p="a*a"))
    print(isMatch(s="aa", p="a*b"))
