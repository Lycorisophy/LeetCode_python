def findAndReplacePattern(words: [str], pattern: str) -> [str]:
    res = []
    np = len(pattern)

    def samepattern(A: str, B: str) -> bool:
        d = dict()
        s = set()
        for a, b in zip(A, B):
            if b not in d:
                if a in s:
                    return False
                d[b] = a
                s.add(a)
            else:
                if d[b] != a:
                    return False
        return True

    for word in words:
        nw = len(word)
        if nw == np and samepattern(pattern, word):
            res.append(word)
    return res


if __name__ == '__main__':
    print(findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))

