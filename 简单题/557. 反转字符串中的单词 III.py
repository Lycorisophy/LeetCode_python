def reverseWords(s: str) -> str:
    words = s.split()
    res = ''
    for word in words:
        if res:
            res += ' '
        res += word[::-1]
    return res


if __name__ == '__main__':
    print(reverseWords("Let's take LeetCode contest"))