def shuffle(self, nums: [int], n: int) -> [int]:
    res = []
    for z in zip(nums[:n], nums[n:]):
        x, y = z
        res.append(x)
        res.append(y)
    return res

