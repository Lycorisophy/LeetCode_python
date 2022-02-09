class DisjointSet:
    def __init__(self, n):
        self.S = list(range(n + 1))

    def find(self, X):
        return self.S[X] if self.S[X] == X else self.find(self.S[X])

    def union(self, X, Y):
        self.S[self.find(X)] = self.find(Y)

def isShift(str1: str, str2: str) -> bool:
    base = (ord(str1[0]) - ord(str2[0])) % 26
    

def groupStrings(strings: [str]) -> [[str]]:
    d = dict()
    for string in strings:
        m = len(string)
        if m not in d:
            d[m] = [string]
        else:
            d[m].append(string)
    tmp = []
    for k, v in d.items():
        if len(v) == 1 or k == 1:
            tmp.append(v)
        else:
            m = len(v)
            ds = DisjointSet(m)
            for i in range(m - 1):
                for j in range(i + 1, m):
                    if ds.find(i) != ds.find(j):
                        if isShift(v[i], v[j]):
                            ds.union(i, j)
            print(ds)
    return d


if __name__ == '__main__':
    print(groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
    print(groupStrings(["abc", "bcd", 'sdg', "acef", "xyz", "az", "ba", "a", "z"]))
    print(groupStrings(["abc", "bcd", 'sdg', "acef", 'cb', "xyz", "az", "ba", "a", "z"]))
