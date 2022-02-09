def numJewelsInStones(jewels: str, stones: str) -> int:
    sj = [0]*52
    a, ca = ord('a'), ord('A')
    for s in jewels:
        os = ord(s)
        if os >= a:
            sj[os-a] = 1
        else:
            sj[26+os-ca] = 1
    n = 0
    for s in stones:
        os = ord(s)
        if os >= a:
            if sj[os - a] == 1:
                n += 1
        else:
            if sj[26 + os - ca] == 1:
                n += 1
    return n


if __name__ == '__main__':
    print(numJewelsInStones("tuMxJ"
,"LApcjt"))

