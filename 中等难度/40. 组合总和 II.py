def combinationSum2(candidates: [int], target: int) -> [[int]]:
    def backtrack(tmp, cur, index):
        if cur > target:
            return
        if cur == target:
            res.append(tmp)
            return
        for i in range(index, n):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            backtrack(tmp + [candidates[i]], cur + candidates[i], i + 1)

    candidates.sort()
    n = candidates.__len__()
    res = []
    backtrack([], 0, 0)
    return res


if __name__ == '__main__':
    print(combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
