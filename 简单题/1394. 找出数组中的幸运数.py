def findLucky(arr: [int]) -> int:
    res = -1
    dic = {}
    for a in arr:
        dic[a] = dic.get(a, 0) + 1
    for key in dic.keys():
        if key == dic[key]:
            res = max(key, res)
    return res


if __name__ == '__main__':
    print(findLucky([1, 2, 2, 3, 3, 3]))
    print(findLucky([5]))
    print(findLucky([7, 7, 7, 7, 7, 7, 7]))
