def findStrobogrammatic(n: int) -> [str]:
    if n < 3:
        if n == 0:
            return []
        elif n == 1:
            return ['0', '1', '8']
        else:
            return ["11", "69", "88", "96"]
    res = []
    a, b = divmod(n, 2)

    def backtrack(tmp, length1, length2):
        m = len(tmp)
        if b == 1 and m == a:
            for j in range(length2):
                backtrack(tmp + [candidates2[j]], length1, length2)
            return
        if m == a + b:
            res.append(tmp)
            return
        for i in range(length1):
            if tmp or candidates[i] != '0':
                backtrack(tmp + [candidates[i]], length1, length2)

    candidates = ['6', '9', '8', '1', '0']
    candidates2 = ['8', '1', '0']
    backtrack([], 5, 3)
    reverseDict = {'6': '9', '9': '6', '8': '8', '0': '0', '1': '1'}
    o = len(res)
    for i in range(o):
        for j in range(a-1, -1, -1):
            res[i].append(reverseDict[res[i][j]])
    ans = [''.join(r) for r in res]
    return ans


if __name__ == '__main__':
    print(findStrobogrammatic(3))
    print(findStrobogrammatic(4))
    print(findStrobogrammatic(5))
    print(findStrobogrammatic(6))
