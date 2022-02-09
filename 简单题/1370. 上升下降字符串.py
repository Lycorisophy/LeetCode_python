from collections import Counter


def sortString(s: str) -> str:
    res = []
    nums = [ord(c) for c in s]
    nums.sort()
    counter = {k: v for k, v in Counter(nums).items()}
    i, n = 0, nums.__len__()
    while res.__len__() < n:
        if i % 2 == 0:
            for k, v in counter.items():
                if v > 0:
                    res.append(k)
                    counter[k] -= 1
        else:
            tmp = []
            for k, v in counter.items():
                if v > 0:
                    tmp.append(k)
                    counter[k] -= 1
            res += tmp[::-1]
        i += 1
    return ''.join([chr(c) for c in res])


if __name__ == '__main__':
    print(sortString("aabbbcccc"))
    print(sortString("rat"))
    print(sortString("leetcode"))
    print(sortString("ggggggg"))
    print(sortString("spo"))
    print(sortString("a"))
