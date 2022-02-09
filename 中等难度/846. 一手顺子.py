def isNStraightHand(hand: [int], groupSize: int) -> bool:
    cnt = collections.Counter(hand)
    while cnt:
        m = min(cnt)
        for k in range(m, m + groupSize):
            v = cnt[k]
            if not v:
                return False
            if v == 1:
                del cnt[k]
            else:
                cnt[k] = v - 1
    return True


if __name__ == '__main__':
    print(isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], W=3))
    print(isNStraightHand(hand=[1, 2, 3, 4, 5], W=4))
