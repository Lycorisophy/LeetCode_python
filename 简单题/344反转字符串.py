def reverseString(s: [str]) -> None:
    s[::-1] = s


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    reverseString(s)
    print(s)