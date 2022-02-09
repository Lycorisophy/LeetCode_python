def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    pos, pos2 = [], []
    l, l2 = [], []
    for i, data in enumerate(s):
        if data in vowels:
            pos.append(i)
            l.append(data)
        else:
            pos2.append(i)
            l2.append(data)
    l = l[::-1]
    res = [0]*(len(l)+len(l2))
    for i, po in enumerate(pos):
        res[po] = l[i]
    for i, po in enumerate(pos2):
        res[po] = l2[i]
    rs = ''
    for i, data in enumerate(res):
        rs += data
    return rs


if __name__ == '__main__':
    print(reverseVowels(s="leetcode"))
