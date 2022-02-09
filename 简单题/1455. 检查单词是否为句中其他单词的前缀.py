def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    sentences = sentence.split()
    n = searchWord.__len__()
    for i, sentence in enumerate(sentences, start=1):
        if sentence.__len__() >= n:
            for s1, s2 in zip(sentence, searchWord):
                if s1 != s2:
                    break
            else:
                return i
    return -1


if __name__ == '__main__':
    print(isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro"))
    print(isPrefixOfWord(sentence="i am tired", searchWord="you"))
    print(isPrefixOfWord(sentence="i use triple pillow", searchWord="pill"))
    print(isPrefixOfWord(sentence="hello from the other side", searchWord="they"))

