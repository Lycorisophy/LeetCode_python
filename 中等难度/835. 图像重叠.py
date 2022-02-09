import collections


def largestOverlap(img1: [[int]], img2: [[int]]) -> int:
    count = collections.Counter()
    for i, row in enumerate(img1):
        for j, v in enumerate(row):
            if v:
                for i2, row2 in enumerate(img2):
                    for j2, v2 in enumerate(row2):
                        if v2:
                            count[i - i2, j - j2] += 1
    return max(count.values() or [0])


if __name__ == '__main__':
    print(largestOverlap(img1=[[1, 1, 0], [0, 1, 0], [0, 1, 0]], img2=[[0, 0, 0], [0, 1, 1], [0, 0, 1]]))
    print(largestOverlap(img1=[[1]], img2=[[1]]))
    print(largestOverlap(img1=[[0]], img2=[[0]]))
