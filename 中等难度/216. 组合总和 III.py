def combinationSum3(k: int, n: int) -> [[int]]:
    def traceback(tmp: [int], last: int, has: int):
        if tmp.__len__() == k - 1:
            rm = n - has
            if rm > last and 0 < rm < 10:
                res.append(tmp+[rm])
            return
        for i in range(1, 10):
            if i > last:
                traceback(tmp + [i], i, has+i)

    res = []
    traceback([], 0, 0)
    return res


if __name__ == '__main__':
    print(combinationSum3(k=3, n=7))
    print(combinationSum3(k=3, n=9))
    print(combinationSum3(k=4, n=30))
