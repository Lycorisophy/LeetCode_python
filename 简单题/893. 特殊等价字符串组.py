from collections import Counter


def numSpecialEquivGroups(A: [str]) -> int:
    def str_sum(strs: [str]):
        res = ''
        for s in strs:
            res += s
        return res
    letters = [[a[::2], a[1::2]] for a in A]
    o_l, e_l = [], []
    for letter in letters:
        o_l.append(str_sum(sorted(letter[0])))
        e_l.append(str_sum(sorted(letter[1])))
    return len(set([o+e for o, e in zip(o_l, e_l)]))


if __name__ == '__main__':
    print(numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
    print(numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))

