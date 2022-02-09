import functools


def respace(dictionary: [str], sentence: str) -> int:
    dict_words = set(dictionary)
    lens = [len(w) for w in dictionary]
    lens.sort(reverse=True)
    n = len(sentence)

    @functools.lru_cache(maxsize=1000)
    def dfs(idx: int, N: int) -> int:
        if idx >= N:
            return 0
        tails = [dfs(idx + length, N) for length in lens
                 if idx + length <= N and sentence[idx:idx + length] in dict_words]
        tails += [1 + dfs(idx + 1, N)]
        return min(tails) if tails else 0

    return dfs(0, n)


if __name__ == '__main__':
    print(respace(dictionary=["looked", "just", "like", "her", "brother"],
                  sentence="jesslookedjustliketimherbrother"))
    print(respace(dictionary=["lookedjustl", "just", "like", "her", "brother"],
                  sentence="jesslookedjustliketimherbrother"))
    print(respace(dictionary=["look", "looked", "just", "like", "her", "brother"],
                  sentence="jesslookedjustliketimherbrother"))
