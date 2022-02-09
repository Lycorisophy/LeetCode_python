def wiggleSort(nums: [int]) -> None:
    n = nums.__len__()
    nums.sort(reverse=True)
    m = n // 2
    for i in range(n//2):
        num = nums.pop(0)
        nums.insert(m+i*2, num)
        m -= 1
    return nums


if __name__ == '__main__':
    print(wiggleSort([1, 5, 1, 1, 6, 4]))
    print(wiggleSort([1, 3, 2, 2, 3, 1]))
    print(wiggleSort([1, 3, 2, 2, 3, 1, 0]))
