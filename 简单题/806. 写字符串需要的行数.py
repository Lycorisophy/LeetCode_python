def numberOfLines(widths: [int], s: str) -> [int]:
    h = 0
    m = 0
    a = ord('a')
    for l in s:
        t = widths[ord(l)-a]
        m += t
        if m > 100:
            m = t
            h += 1
        elif m == 100:
            m = 0
            h += 1
    return [h+1, m] if m != 0 else [h, 100]


if __name__ == '__main__':
    print(numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
,s = "abcdefghijklmnopqrstuvwxyz"
))
    print(numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
,s = "bbbcccdddaaa"))

