def arrayNesting(nums: [int]) -> int:
    n = nums.__len__()
    visited = [False] * n
    res = 0
    for i in range(n):
        if not visited[i]:
            start = nums[i]
            cnt = 0
            start = nums[start]
            cnt += 1
            visited[start] = True
            while start != nums[i]:
                start = nums[start]
                cnt += 1
                visited[start] = True
            res = max(res, cnt)
    return res


if __name__ == '__main__':
    print(arrayNesting([5, 4, 0, 3, 1, 6, 2]))
