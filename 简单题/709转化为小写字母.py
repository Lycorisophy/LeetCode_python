def toLowerCase(str: str) -> str:
    dic = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
                   'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
                   'M':'m', 'N':'n', 'O':'o','P':'p', 'Q':'q', 'R':'r',
                   'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
                   'Y':'y', 'Z':'z'}
    res = ''
    for s in str:
        res += dic[s] if s in dic else s
    return res


if __name__ == '__main__':
    print(toLowerCase("Hello"))
    print(toLowerCase("here"))
    print(toLowerCase("LOVELY"))


