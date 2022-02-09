import copy


def decrypt(code: [int], k: int) -> [int]:
    n = code.__len__()
    res = [0] * n
    if k == 0:
        return res
    if k > 0:
        for i in range(n):
            for j in range(1, k + 1):
                res[i] += code[(n + i + j) % n]
        return res
    for i in range(n):
        for j in range(1, -k + 1):
            res[i] += code[(n + i - j) % n]
    return res


if __name__ == '__main__':
    print(decrypt(code = [5,7,1,4], k = 3))
    print(decrypt(code = [1,2,3,4], k = 0))
    print(decrypt(code = [2,4,9,3], k = -2))
