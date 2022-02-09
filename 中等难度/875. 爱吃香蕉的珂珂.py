def minEatingSpeed(piles: [int], h: int) -> int:
    left, right = 1, max(piles)
    while right > left:
        mid = int(left + (right - left) / 2)
        s = 0
        for pile in piles:
            a, b = divmod(pile, mid)
            s += a
            if b != 0:
                s += 1
        if s > h:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    print(minEatingSpeed([3, 6, 7, 11], 8))
    print(minEatingSpeed([30, 11, 23, 4, 20], 5))
    print(minEatingSpeed([30, 11, 23, 4, 20], 6))
