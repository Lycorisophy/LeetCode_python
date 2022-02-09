def findShortestSubArray(nums: [int]) -> int:
    count = {}
    for i, n in enumerate(nums):
        try:
            count[n][0] += 1
            count[n][2] = i
        except KeyError:
            count[n] = [1, i, i]
    max_c = 0
    for v in count.values():
        if v[0] > max_c:
            max_c = v[0]
            res = v[2]-v[1]
        elif v[0] == max_c:
            res = min(v[2]-v[1], res)
    return res+1


if __name__ == '__main__':
    print(findShortestSubArray([1, 2, 2, 3, 1]))
