def decompressRLElist(nums: [int]) -> [int]:
    return [val for freq, val in zip(nums[::2], nums[1::2]) for _ in range(freq)]


if __name__ == '__main__':
    print(decompressRLElist([1, 2, 3, 4]))
    print(decompressRLElist([1, 1, 2, 3]))
