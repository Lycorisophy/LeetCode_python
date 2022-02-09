def findLHS(nums: [int]) -> int:
    map = {}
    for num in nums:
        try:
            map[num] += 1
        except KeyError:
            map[num] = 1
    sorted(map.keys())
    res = [map[key+1]+val for key, val in map.items() if key+1 in map]
    return max(res) if res else 0


if __name__ == '__main__':
    print(findLHS([1,3,2,2,5]))