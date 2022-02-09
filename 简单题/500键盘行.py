def findWords(words: [str]) -> [str]:
    qwe = ['Q','W','E','R','T','Y','U','I','O','P','q','w','e','r','t','y','u','i','o','p']
    asd = ['A','S','D','F','G','H','J','K','L','a','s','d','f','g','h','j','k','l']
    zxc = ['Z','X','C','V','B','N','M','z','x','c','v','b','n','m']
    t = [1]*len(words)
    for i, word in enumerate(words):
        cq, ca, cz = 0, 0, 0
        if len(word) >= 1:
            for letter in word:
                if letter in qwe:
                    cq = 1
                    if ca == 1 or cz == 1:
                        t[i] = 0
                        break
                if letter in asd:
                    ca = 1
                    if cq == 1 or cz == 1:
                        t[i] = 0
                        break
                if letter in zxc:
                    cz = 1
                    if cq == 1 or ca == 1:
                        t[i] = 0
                        break
    res = []
    for i, word in enumerate(words):
        if t[i] == 1:
            res.append(word)
    return res



if __name__ == '__main__':
    print(findWords(words=["Hello","Alaska","Dad","Peace"]))
