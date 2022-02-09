def detectCapitalUse(word: str) -> bool:
    a, b, c, d = 0, 0, 0, 0
    for letter in word:
        if letter.isupper():
            if a == 1 or c == 1:
                return False
            if d != 0:
                b = 1
        else:
            if d == 0:
                a = 1
            else:
                if b == 1:
                    return False
                c = 1
        d += 1
    return True


if __name__ == '__main__':
    print(detectCapitalUse("DD"))