def getValidT9Words(num: str, words: [str]) -> [str]:
    dict = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7', '7', '7', '7', '8',
            '8', '8', '9', '9', '9', '9']
    res = []
    a = ord('a')
    for word in words:
        word_str = ''
        for char in word:
            word_str += dict[ord(char)-a]
        if word_str == num:
            res.append(word)
    return res


if __name__ == '__main__':
    print(getValidT9Words(num="8733", words=["tree", "used"]))
    print(getValidT9Words(num="2", words=["a", "b", "c", "d"]))
