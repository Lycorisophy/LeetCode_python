def partitionLabels(s: str) -> [int]:
    res = []
    disjoint = [0] * 26
    m = 1
    a = ord('a')
    n = s.__len__()
    disjoint[ord(s[0]) - a] = 1
    for c in s:
        t = disjoint[ord(c)-a]
        if t != 0:
            m = t
            for i in range(26):
                disjoint[i] = min(disjoint[i], t)
        else:
            m += 1
            disjoint[ord(c)-a] = m
    start = 0
    for i in range(1, n):
        if disjoint[ord(s[i])-a] != disjoint[ord(s[i-1])-a]:
            res.append(i-start)
            start = i
    res.append(n-start)
    return res


if __name__ == '__main__':
    print(partitionLabels("ababcbacadefegdehijhklij"))

