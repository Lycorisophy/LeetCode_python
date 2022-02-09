# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
def countSegments(s: str) -> int:
    s = s.split(' ')
    c = 0
    for i in s:
        if i != '':
            c += 1
    return c


if __name__ == '__main__':
    print(countSegments("The one-hour drama series Westworld is a dark odyssey about the dawn of artificial "
                        "consciousness and the evolution of sin. Set at the intersection of the near future and the "
                        "reimagined past, it explores a world in "
                        "which every human appetite, no matter how noble or depraved, can be indulged."))