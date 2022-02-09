def removeDuplicateLetters(s: str) -> str:
    letters = {}
    for char in s:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    res = []
    for char in s:
        if char not in res:
            while res:
                top = res[-1]
                if letters[top] > 1 and top > char:
                    res.pop(-1)
                    letters[top] -= 1
                else:
                    break
            res.append(char)
        else:
            letters[char] -= 1
    return ''.join(res)


if __name__ == '__main__':
    print(removeDuplicateLetters("bbcaac"))
    print(removeDuplicateLetters("abacb"))
    print(removeDuplicateLetters("cdadabcc"))
    print(removeDuplicateLetters("bcabc"))
    print(removeDuplicateLetters("cbacdcbc"))

