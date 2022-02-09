def validUtf8(data: [int]) -> bool:
    n = data.__len__()
    i = 0
    while i < n:
        d = data[i]
        d = format(d, '#010b')[-8:]
        cnt = 0
        for a in d:
            if a == '0':
                break
            else:
                cnt += 1
        if cnt > 4 or cnt == 1:
            return False
        elif cnt == 0:
            i += 1
        else:
            i += cnt
            if i > n:
                return False
            j = i - 1
            while cnt > 1:
                d = data[j]
                d = format(d, '#010b')[-8:]
                if d[:2] != '10':
                    return False
                j -= 1
                cnt -= 1
    return True


if __name__ == '__main__':
    print(validUtf8([235, 140, 4]))
    print(validUtf8([197, 130, 1]))
