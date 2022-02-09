def shortestWordDistance(wordsDict: [str], word1: str, word2: str) -> int:
    n = len(wordsDict)
    res = n
    if word1 == word2:
        w = list()
        for i, word in enumerate(wordsDict):
            if word == word1:
                w.append(i)
        n3 = len(w)
        for i in range(1, n3):
            res = min(res, w[i]-w[i-1])
        return res
    w1, w2 = list(), list()
    for i, word in enumerate(wordsDict):
        if word == word1:
            w1.append(i)
        if word == word2:
            w2.append(i)
    n1, n2 = len(w1), len(w2)
    i, j = 0, 0
    while i < n1 and j < n2:
        d1, d2 = w1[i], w2[j]
        if d1 < d2:
            res = min(res, d2 - d1)
            i += 1
        else:
            res = min(res, d1 - d2)
            j += 1
    return res


if __name__ == '__main__':
    print(shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], word1 = 'makes', word2 = 'coding'))
    print(shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"))
