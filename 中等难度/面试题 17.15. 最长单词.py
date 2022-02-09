def longestWord(words: [str]) -> str:
    words.sort(key=lambda x: (-len(x), x))
    set_words = set(words)

    def dfs(s: str, idx: int, wordCnt: int) -> bool:
        n = len(s)
        if idx >= n:
            return wordCnt > 1
        for i in range(idx, n):
            substr = s[idx:i + 1]
            if substr in set_words and dfs(s, i + 1, wordCnt + 1):
                return True
        return False

    for word in words:
        if dfs(word, 0, 0):
            return word
    return ''


if __name__ == '__main__':
    print(longestWord(["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]))
