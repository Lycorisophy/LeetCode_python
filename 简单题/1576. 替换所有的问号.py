def modifyString(s: str) -> str:
    s = list(s)
    n = s.__len__()
    dic = ['a', 'b', 'c']
    for i, char in enumerate(s):
        if char == '?':
            if i != 0:
                pre = s[i-1]
            else:
                pre = ''
            if i != n-1:
                nxt = s[i+1]
            else:
                nxt = ''
            for d in dic:
                if d != pre and d != nxt:
                    s[i] = d
                    break
    return ''.join(s)


if __name__ == '__main__':
    print(modifyString(s = "ubv?w"))
    print(modifyString("j?qg??b"))
    print(modifyString("??yw?ipkj?"))
