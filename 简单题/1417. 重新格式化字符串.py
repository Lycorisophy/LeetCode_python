def reformat(s: str) -> str:
    nums, letters = [], []
    for char in s:
        if char.isnumeric():
            nums.append(char)
        else:
            letters.append(char)
    n, m = nums.__len__(), letters.__len__()
    if n == 0:
        if m == 1:
            return letters[0]
        return ''
    if m == 0:
        if n == 1:
            return nums[0]
        return ''

    def mix(arr1: [str], arr2: [str], ans='') -> str:
        for a1, a2 in zip(arr1, arr2):
            ans += a1 + a2
        return ans

    if n > m:
        tmp = n - m
        if tmp > 1:
            return ''
        return mix(letters, nums, nums[-1])
    if m > n:
        tmp = m - n
        if tmp > 1:
            return ''
        return mix(nums, letters, letters[-1])
    return mix(nums, letters)


if __name__ == '__main__':
    print(reformat("j"))
    print(reformat("a0b1c2"))
    print(reformat("leetcode"))
    print(reformat("1229857369"))
    print(reformat("covid2019"))
    print(reformat("ab123"))

