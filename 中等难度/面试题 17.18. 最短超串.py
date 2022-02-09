def shortestSeq(big: [int], small: [int]) -> [int]:
    small_set = {s for s in small}
    m = len(small)
    d = {s: 0 for s in small}
    left = 0
    cnt = 0
    res = [0, 100000]
    for right, b in enumerate(big):
        if b not in small_set:
            continue
        d[b] += 1
        if d[b] == 1:
            cnt += 1
        if cnt == m:
            while big[left] not in small_set or d[big[left]] > 1:
                if big[left] in small_set:
                    d[big[left]] -= 1
                left += 1
            if right - left < res[1] - res[0]:
                res = [left, right]
    return res if res != [0, 100000] else []


if __name__ == '__main__':
    print(shortestSeq(big=[7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7],
                      small=[1, 5, 9]))
    print(shortestSeq(big=[1, 2, 3],
                      small=[4]))
