def combinationSum(candidates: [int], target: int) -> [[int]]:
    def dfs(candidates, begin, length, path, res, target):
        for i in range(begin, length):
            data = candidates[i]
            if target > data:
                dfs(candidates, i, length, path + [data], res, target - data)
            elif target == data:
                path += [data]
                res.append(path)

    candidates.sort()
    n = candidates.__len__()
    path = []
    res = []
    dfs(candidates, 0, n, path, res, target)
    return res


if __name__ == '__main__':
    print(combinationSum(candidates=[2, 7, 6, 3, 5, 1], target=9))
    print(combinationSum(candidates=[2, 3, 5], target=8))
