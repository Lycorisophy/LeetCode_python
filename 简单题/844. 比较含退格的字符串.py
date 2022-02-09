def backspaceCompare(S: str, T: str) -> bool:
    i, j = len(S) - 1, len(T) - 1
    skip_s, skip_t = 0, 0
    while i > -1 and j > -1:
        s, t = S[i], T[j]
        if s == '#':
            skip_s += 1
            i -= 1
            s_can_com = False
        else:
            if skip_s > 0:
                s_can_com = False
                skip_s -= 1
                i -= 1
            else:
                s_can_com = True
        if t == '#':
            skip_t += 1
            j -= 1
            t_can_com = False
        else:
            if skip_t > 0:
                t_can_com = False
                skip_t -= 1
                j -= 1
            else:
                t_can_com = True
        if s_can_com and t_can_com:
            if s != t:
                return False
            i -= 1
            j -= 1
    print(i == j)
    print(skip_s == skip_t)
    print(s_can_com==t_can_com)
    return True


if __name__ == '__main__':
    print(backspaceCompare("bbbextm"
,"bbb#extm"))

