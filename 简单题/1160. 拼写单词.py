from collections import Counter


def countCharacters(words: [str], chars: str) -> int:
    res = 0
    o_chars = dict(Counter(chars))
    for word in words:
        chars = o_chars.copy()
        for letter in word:
            if letter not in chars:
                break
            if chars[letter] == 0:
                break
            chars[letter] -= 1
        else:
            res += word.__len__()
    return res
# def countCharacters(words: [str], chars: str) -> int:
#     res = 0
#     a = ord('a')
#     o_chars = [0]*26
#     for char in chars:
#         o_chars[ord(char)-a] += 1
#     for word in words:
#         chars = o_chars.copy()
#         for char in word:
#             if chars[ord(char) - a] == 0:
#                 break
#             chars[ord(char) - a] -= 1
#         else:
#             res += word.__len__()
#     return res


if __name__ == '__main__':
    print(countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
    print(countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))
