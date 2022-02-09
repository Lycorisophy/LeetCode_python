def combine(n: int, k: int) -> [[int]]:
    def backtrack(tmp, index):
        if tmp.__len__() == k:
            res.append(tmp)
            return
        for i in range(index, n):
            backtrack(tmp + [candidates[i]], i + 1)

    candidates = [i for i in range(1, n + 1)]
    res = []
    backtrack([], 0)
    return res





if __name__ == '__main__':
    print(combine(6, 4))
