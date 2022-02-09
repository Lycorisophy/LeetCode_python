def countLargestGroup(n: int) -> int:
    dic = {}
    for i in range(1, n+1):
        S = str(i)
        a = sum([int(s) for s in S])
        dic[a] = dic.get(a, 0) + 1
    resList = list(dic.values())
    return resList.count(max(resList))


if __name__ == '__main__':
    print(countLargestGroup(13))
    print(countLargestGroup(2))
    print(countLargestGroup(15))
    print(countLargestGroup(24))
