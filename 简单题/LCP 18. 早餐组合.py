def breakfastNumber(staple: [int], drinks: [int], x: int) -> int:
    staple.sort()
    drinks.sort()

    def search(nums: [int], n: int, target: int) -> int:
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return l

    i = search(staple, staple.__len__(), x)
    j = search(drinks, drinks.__len__(), x)
    staple = staple[:i]
    drinks = drinks[:j]
    manys = {}

    def howmany(t: int, nums: [int]) -> int:
        n = nums.__len__()
        k = search(nums, n, x-t+1)
        return k

    res = 0
    for s in staple:
        if s in manys:
            res += manys[s]
        else:
            many = howmany(s, drinks)
            manys[s] = many
            res += many
    return res % 1000000007


if __name__ == '__main__':
    print(breakfastNumber(staple = [2,1,1], drinks = [8,9,5,1], x = 9))


