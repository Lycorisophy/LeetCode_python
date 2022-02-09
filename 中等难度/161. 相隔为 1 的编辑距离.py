def isOneEditDistance(s: str, t: str) -> bool:
    ls, lt = len(s), len(t)
    st = ls - lt
    if st == -1:
        if ls == 0:
            return True
        j = 0
        for i in range(lt):
            if t[i] == s[j]:
                j += 1
                if j == ls:
                    return True
    elif st == 0:
        if ls == 0:
            return False
        cnt = 0
        for S, T in zip(s, t):
            if S != T:
                cnt += 1
                if cnt == 2:
                    return False
        return True if cnt == 1 else False
    elif st == 1:
        if lt == 0:
            return True
        j = 0
        for i in range(ls):
            if s[i] == t[j]:
                j += 1
                if j == lt:
                    return True
    return False


if __name__ == '__main__':
    print(isOneEditDistance(s = "ab", t = "acb"))
    print(isOneEditDistance(s = "cab", t = "ad"))
    print(isOneEditDistance(s = "1203", t = "1213"))
