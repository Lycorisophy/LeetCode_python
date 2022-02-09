def isLongPressedName(name: str, typed: str) -> bool:
    l1, l2 = name.__len__(), typed.__len__()
    i, j = 0, 0
    tmp = ''
    while i < l1 and j < l2:
        if typed[j] == name[i]:
            tmp = name[i]
            i += 1
        elif typed[j] != tmp:
            return False
        j += 1
    if i != l1:
        return False
    elif j == l2:
        return True
    else:
        for k in range(j, l2):
            if typed[k] != tmp:
                return False
        return True


if __name__ == '__main__':
    print(isLongPressedName(name = "laiden", typed = "laiden"))

