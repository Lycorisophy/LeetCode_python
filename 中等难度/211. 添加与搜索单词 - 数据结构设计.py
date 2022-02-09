class WordDictionary:

    def __init__(self):
        self.dic = {}

    def addWord(self, word: str) -> None:
        n = word.__len__()
        if n not in self.dic:
            self.dic[n] = [word]
        else:
            self.dic[n].append(word)

    def search(self, word: str) -> bool:
        n = word.__len__()

        def isSame(A: str, B: str) -> bool:
            for a, b in zip(A, B):
                if a != '.':
                    if a != b:
                        return False
            return True

        if n not in self.dic:
            return False
        for v in self.dic[n]:
            if isSame(word, v):
                return True
        return False


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))
    print(wordDictionary.search("bad"))
    print(wordDictionary.search(".ad"))
    print(wordDictionary.search("b.."))
