from collections import Counter


def findSpecialInteger(arr: [int]) -> int:
    for key, num in Counter(arr).items():
        if num > len(arr) // 4:
            return key