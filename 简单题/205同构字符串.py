def isIsomorphic(s: str, t: str) -> bool:
    p1, p2 = [], []
    for data1, data2 in zip(s, t):
        if data1 not in p1:
            if data2 in p2:
                return False
            p1.append(data1)
            p2.append(data2)
        else:
            if p2[p1.index(data1)] != data2:
                return False
    return True


if __name__ == '__main__':
    print(isIsomorphic(s = "badc", t = "baba"))