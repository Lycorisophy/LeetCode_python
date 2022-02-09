def reorderSpaces(text: str) -> str:
    words = []
    tmp = ''
    cnt = 0
    for char in text:
        if char == ' ':
            cnt += 1
            if tmp != '':
                words.append(tmp)
                tmp = ''
        else:
            tmp += char
    if tmp != '':
        words.append(tmp)
    n = words.__len__()
    if n == 0:
        return ''
    if n == 1:
        return words[0]+' '*cnt
    n -= 1
    res = ''
    n_space, other_space = divmod(cnt, n)
    for i, word in enumerate(words):
        res += word
        if i != n:
            res += ' '*n_space
    return res + ' '*other_space


if __name__ == '__main__':
    print(reorderSpaces("  this   is  a sentence "))
    print(reorderSpaces(" practice   makes   perfect"))
    print(reorderSpaces("hello   world"))
    print(reorderSpaces("  walks  udp package   into  bar a"))
    print(reorderSpaces("a"))
