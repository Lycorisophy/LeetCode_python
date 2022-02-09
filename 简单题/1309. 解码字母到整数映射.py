def freqAlphabets(s: str) -> str:
    res = ''
    i = s.__len__()-1
    while i > -1:
        if s[i] == '#':
            res += chr(96+int(s[i-2]+s[i-1]))
            i -= 3
        else:
            res += chr(96+int(s[i]))
            i -= 1
    return res[::-1]


if __name__ == '__main__':
    print(freqAlphabets("10#11#12"))
    print(freqAlphabets("1326#"))
    print(freqAlphabets("25#"))
    print(freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))

