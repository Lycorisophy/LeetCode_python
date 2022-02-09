def isAlienSorted(words: [str], order: str) -> bool:
    dic = {letter: i for i, letter in enumerate(order)}
    pre_word = words[0]
    for word in words[1:]:
        for l1, l2 in zip(word, pre_word):
            t1, t2 = dic[l1], dic[l2]
            if t1 < t2:
                return False
            elif t1 > t2:
                break
        else:
            if pre_word.__len__() > word.__len__():
                return False
        pre_word = word
    return True


if __name__ == '__main__':
    print(isAlienSorted(["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
    print(isAlienSorted(["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
    print(isAlienSorted(["kuvp","q"]
,"ngxlkthsjuoqcpavbfdermiywz"))
