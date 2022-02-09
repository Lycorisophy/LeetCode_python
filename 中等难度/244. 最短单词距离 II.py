class WordDistance:

    def __init__(self, wordsDict: [str]):
        self.dict = dict()
        for i, word in enumerate(wordsDict):
            if word not in self.dict:
                self.dict[word] = [i]
            else:
                self.dict[word].append(i)
        self.n = len(wordsDict)

    def shortest(self, word1: str, word2: str) -> int:
        res = self.n
        w1, w2 = self.dict[word1], self.dict[word2]
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
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    obj = WordDistance(wordsDict)
    print(obj.shortest(word1 = 'coding', word2 = 'practice'))
    print(obj.shortest(word1 = "makes", word2 = "coding"))
