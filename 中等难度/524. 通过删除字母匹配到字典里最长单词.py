def findLongestWord(s: str, dictionary: [str]) -> str:
    ns = len(s)
    res = ''
    nr = 0

    def ispart(A: str, a: str, na: int, nA: int) -> bool:
        i, j = 0, 0
        while i < na and j < nA:
            ca, cA = a[i], A[j]
            if ca == cA:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == na else False

    for d in dictionary:
        nd = len(d)
        if nd >= nr and ispart(s, d, nd, ns):
            if nd == nr:
                if d < res:
                    res = d
            else:
                res = d
                nr = nd
    return res


if __name__ == '__main__':
    print(findLongestWord(s="abpcplea", dictionary=["ale", "apple", "monkey", "plea"]))
    print(findLongestWord(s="abpcplea", dictionary=["a", "b", "c"]))
