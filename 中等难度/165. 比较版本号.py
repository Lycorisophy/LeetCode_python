def compareVersion(version1: str, version2: str) -> int:
    v1, v2 = version1.split('.'), version2.split('.')
    v1, v2 = [int(num) for num in v1], [int(num) for num in v2]
    for i, v in enumerate(zip(v1, v2)):
        a1, a2 = v
        if a1 > a2:
            return 1
        elif a1 < a2:
            return -1
    n1 = v1.__len__()
    i += 1
    if n1 > i:
        more = v1[i:]
        for m in more:
            if m > 0:
                return 1
    else:
        more = v2[i:]
        for m in more:
            if m > 0:
                return -1
    return 0




if __name__ == '__main__':
    print(compareVersion(version1="1.01", version2="1.001"))
    print(compareVersion(version1="1.0", version2="1.0.0"))
    print(compareVersion(version1="0.1", version2="1.1"))
    print(compareVersion(version1 = "1.0.1", version2 = "1"))
    print(compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))
    print(compareVersion(version1="1.0.0.1", version2="1"))
