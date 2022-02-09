def buildArray(target: [int], n: int) -> [str]:
    res = []
    cnt = 0
    tl = target.__len__()
    for i in range(1, n + 1):
        if i in target:
            res.append('Push')
            cnt += 1
            if cnt == tl:
                return res
        else:
            res.append('Push')
            res.append('Pop')
    return res


if __name__ == '__main__':
    print(buildArray(target=[1, 3], n=3))
    print(buildArray(target=[1, 2, 3], n=3))
    print(buildArray(target=[1, 2], n=4))
    print(buildArray(target=[2, 3, 4], n=4))

