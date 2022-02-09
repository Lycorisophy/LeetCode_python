def isOneBitCharacter(bits: [int]) -> bool:
    i = 0
    res = []
    while i < len(bits):
        if bits[i] == 1:
            i += 1
        i += 1
        res.append(i)
    try:
        return res[-1] - res[-2] == 1
    except IndexError:
        return res[0] == 1


if __name__ == '__main__':
    print(isOneBitCharacter([1, 0]))

