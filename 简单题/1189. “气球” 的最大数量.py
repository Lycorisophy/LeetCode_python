def maxNumberOfBalloons(text: str) -> int:
    res = {'b': .0, 'a': .0, 'l': .0, 'o': .0, 'n': .0}
    for t in text:
        if t in ['b', 'a', 'n']:
            res[t] += 1
        elif t in ['l', 'o']:
            res[t] += 0.5
    return int(min(res.values()))


if __name__ == '__main__':
    print(maxNumberOfBalloons("nlaebolko"))
    print(maxNumberOfBalloons("loonbalxballpoon"))
    print(maxNumberOfBalloons("leetcode"))
