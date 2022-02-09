class Trie:
    def __init__(self, words):
        self.d = {}
        for i in range(len(words)):
            tree = self.d
            for char in words[i]:
                if char not in tree:
                    tree[char] = {}
                tree = tree[char]
            tree['end'] = i

    def search(self, s):
        tree = self.d
        res = []
        for char in s:
            if char not in tree:
                return res
            tree = tree[char]
            if 'end' in tree:
                res.append(tree['end'])
        return res


def multiSearch(big: str, smalls: [str]) -> [[int]]:
    trie = Trie(smalls)
    res = [[] for _ in range(len(smalls))]
    for i in range(len(big)):
        tmp = trie.search(big[i:])
        for idx in tmp:
            res[idx].append(i)
    return res


if __name__ == '__main__':
    print(multiSearch(big="mississippi",
                      smalls=["is", "ppi", "hi", "sis", "i", "ssippi"]))
    print(multiSearch(big="mississippiis",
                      smalls=["", "ppi", "hi", "sis", "i", "ssippi"]))
    print(multiSearch(big="mississippi",
                      smalls=["is", "ppi", "sis", "i", "ssippi"]))
