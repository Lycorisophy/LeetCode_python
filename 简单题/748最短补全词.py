def shortestCompletingWord(licensePlate: str, words: [str]) -> str:
    abc = [0] * 26
    a, ca, z, cz = ord('a'), ord('A'), ord('z'), ord('Z')
    for lp in licensePlate:
        olp = ord(lp)
        if a <= olp <= z:
            abc[olp - a] += 1
        elif ca <= olp <= cz:
            abc[olp - ca] += 1
    res = []
    for word in words:
        cabc = abc.copy()
        for letter in word:
            cabc[ord(letter) - a] -= 1
        if all(i <= 0 for i in cabc):
            res.append(word)
    ans = res[0]
    l = len(ans)
    for i in range(1, len(res)):
        t = res[i]
        tl = len(t)
        if tl < l:
            l = tl
            ans = t
    return ans


if __name__ == '__main__':
    print(shortestCompletingWord(licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]))
    print(shortestCompletingWord(licensePlate="1s3 456", words=["looks", "pest", "stew", "show"]))
    print(shortestCompletingWord(licensePlate="Ah71752",
                                 words=["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent",
                                        "writer", "old"]))
    print(shortestCompletingWord(licensePlate="OgEu755",
                                 words=["enough", "these", "play", "wide", "wonder", "box", "arrive", "money", "tax",
                                        "thus"]))
    print(shortestCompletingWord(licensePlate="iMSlpe4",
                                 words=["claim", "consumer", "student", "camera", "public", "never", "wonder", "simple",
                                        "thought", "use"]))
