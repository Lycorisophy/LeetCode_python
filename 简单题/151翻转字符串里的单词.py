def reverseWords(s: str) -> str:
    s2 = []
    res = ''
    tmp = ''
    pre = 0
    l = len(s)
    for i, data in enumerate(s):
        if str(data).isalpha():
            tmp += data
            pre = 1
            if i == l-1:
                s2.append(tmp)
        elif data == ' ':
            if pre == 1:
                s2.append(tmp)
                tmp = ''
            pre = 0
        else:
            tmp += data
            pre = 1
            if i == l-1:
                s2.append(tmp)
    for i in range(len(s2)-1, -1, -1):
        res += s2[i]
        if i != 0:
            res += ' '
    return res


if __name__ == "__main__":
    print(reverseWords(" Alice! does    not  even like bob!"))
