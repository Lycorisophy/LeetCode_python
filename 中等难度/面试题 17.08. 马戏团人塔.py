import bisect


def bestSeqAtIndex(height: [int], weight: [int]) -> int:
    n = len(height)
    people = sorted(zip(height, weight), key=lambda x: (x[0], -x[1]))
    dp = [0] * n
    res = 0
    for person in people:
        h, w = person
        i = bisect.bisect_left(dp, w, 0, res)
        dp[i] = w
        if i == res:
            res += 1
    return res



if __name__ == '__main__':
    print(bestSeqAtIndex([2868,5485,1356,1306,6017,8941,7535,4941,6331,6181],
[5042,3995,7985,1651,5991,7036,9391,428,7561,8594]))
    print(bestSeqAtIndex(height=[65, 80, 56, 75, 60, 68], weight=[100, 150, 90, 190, 95, 110]))
    print(bestSeqAtIndex(height=[65, 70, 70, 75, 60, 68], weight=[100, 150, 90, 190, 95, 110]))
