def arrayRankTransform(arr: [int]) -> [int]:
    sorted_arr = sorted(list(set(arr.copy())))
    hash_arr = {s: i for i, s in enumerate(sorted_arr, start=1)}
    res = [hash_arr[key] for key in arr]
    return res


if __name__ == '__main__':
    print(arrayRankTransform([40, 10, 20, 30]))
    print(arrayRankTransform([100, 100, 100]))
    print(arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
