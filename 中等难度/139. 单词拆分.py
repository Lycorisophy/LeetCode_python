import functools


def wordBreak(s: str, wordDict: [str]) -> bool:
    n = s.__len__()
    if n == 0:
        return True
    word_dict = {}
    for word in wordDict:
        first = word[0]
        if first not in word_dict:
            word_dict[first] = set()
        word_dict[first].add(word)

    @functools.lru_cache(None)
    def backtrack(S):
        if not S:
            return True

        res = False
        m = S.__len__() + 1
        for i in range(1, m):
            st = S[:i]
            f = st[0]
            if f in word_dict:
                if st in word_dict[f]:
                    res = backtrack(S[i:]) or res
            else:
                break
        return res

    return backtrack(s)


if __name__ == '__main__':
    print(wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
