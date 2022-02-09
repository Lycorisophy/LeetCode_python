from functools import lru_cache


def sortByBits(arr: [int]) -> [int]:
    @lru_cache(None)
    def count(e):
        return bin(e).count("1")

    arr.sort(key=lambda e: (count(e), e))
    return arr


if __name__ == '__main__':
    print(sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
    print(sortByBits([10000, 10000]))
    print(sortByBits([10, 100, 1000, 10000]))
