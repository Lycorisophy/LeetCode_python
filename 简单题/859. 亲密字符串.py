def buddyStrings(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False
    idx = []
    i = 0
    for a, b in zip(A, B):
        if a != b:
            idx.append(i)
        i += 1
    if len(idx) == 2:
        return A[idx[0]] == B[idx[1]] and A[idx[1]] == B[idx[0]]
    if len(idx) == 0:
        return False if len(A) == len(set(A)) else True
    return False


if __name__ == '__main__':
    print(buddyStrings(A="aa", B="aa"))
    print(buddyStrings(A="ab", B="ab"))
    print(buddyStrings(A="aaaaaaabc", B="aaaaaaacb"))
