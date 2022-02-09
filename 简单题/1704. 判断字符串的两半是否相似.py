def halvesAreAlike(s: str) -> bool:
    yy = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    hn = s.__len__()//2
    ny = 0
    for i, char in enumerate(s):
        if i < hn:
            if char in yy:
                ny += 1
        else:
            if char in yy:
                ny -= 1
    return ny == 0


if __name__ == '__main__':
    print(halvesAreAlike("book"))
    print(halvesAreAlike("textbook"))
    print(halvesAreAlike("MerryChristmas"))
