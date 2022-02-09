def findOcurrences(text: str, first: str, second: str) -> [str]:
    words = text.split()
    i = 0
    n = words.__len__()
    index = 0
    res = []
    while i < n:
        tmp = words[i]
        if index == 0:
            if tmp == first:
                index = 1
        elif index == 1:
            if tmp == second:
                index = 2
            elif tmp == first:
                index = 1
            else:
                index = 0
        else:
            res.append(tmp)
            if tmp == first:
                index = 1
            else:
                index = 0
        i += 1
    return res


if __name__ == '__main__':
    print(findOcurrences("alice is a good girl she is a good student", first="a", second="good"))
    print(findOcurrences(text="we will we will rock you", first="we", second="will"))
