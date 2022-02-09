def compress(chars: [str]) -> int:
    anchor = write = 0
    n = chars.__len__()
    for i, char in enumerate(chars):
        if i + 1 == n or chars[i+1] != char:
            chars[write] = chars[anchor]
            write += 1
            if i > anchor:
                for digit in str(i - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = i + 1
    for _ in range(n-write):
        chars.pop(-1)
    return write


if __name__ == '__main__':
    print(compress(["b", "b", "b", "c", "c", "a"]))
    print(compress(["a"]))
    print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
