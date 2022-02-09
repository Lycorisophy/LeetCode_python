from functools import lru_cache


def findTheDistanceValue(arr1: [int], arr2: [int], d: int) -> int:
    @lru_cache(None)
    def isDinstanceValue(a: int) -> bool:
        for a2 in arr2:
            if abs(a-a2) <= d:
                return False
        return True

    return sum(isDinstanceValue(a1) for a1 in arr1)


if __name__ == '__main__':
    print(findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
    print(findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))
