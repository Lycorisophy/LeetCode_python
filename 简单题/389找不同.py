# 给定两个字符串 s 和 t，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。

def findTheDifference(s: str, t: str) -> str:
    m = {}
    for i, data in enumerate(t):
        try:
            m[data] += 1
        except KeyError:
            m[data] = 1
    for i, data in enumerate(s):
        m[data] -= 1
    for k, v in m.items():
        if v == 1:
            return k

if __name__ == '__main__':
    print(findTheDifference(s = "abcd", t = "abcde"))