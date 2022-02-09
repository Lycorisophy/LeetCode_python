def stringMatching(words: [str]) -> [str]:
    res = []
    words.sort(key=lambda x: x.__len__())
    for i, word in enumerate(words[:-1]):
        for other_word in words[i+1:]:
            if word in other_word:
                res.append(word)
                break
    return res


if __name__ == '__main__':
    print(stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
    print(stringMatching(words=["mass", "as", "hero", "superhero"]))
    print(stringMatching(words=["leetcode", "et", "code"]))
    print(stringMatching(words=["blue", "green", "bu"]))
