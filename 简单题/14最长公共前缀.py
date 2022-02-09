def longestCommonPrefix(strs: [str]) -> str:
    res = ''
    for i in zip(*strs):
        if len(set(i)) == 1:
            res += i[0]
        else:
            return res
    return res


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix([]))
    print(longestCommonPrefix(["flower","","flight"]))
