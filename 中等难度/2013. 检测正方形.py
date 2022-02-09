from collections import defaultdict, Counter


class DetectSquares:

    def __init__(self):
        self.dict = defaultdict(Counter)

    def add(self, point: [int]) -> None:
        x, y = point
        self.dict[y][x] += 1

    def count(self, point: [int]) -> int:
        x, y = point
        if y not in self.dict:
            return 0
        res = 0
        col_cnt = self.dict[y]
        for col, cnt in self.dict.items():
            if col != y:
                d = col - y
                res += cnt[x] * col_cnt[x + d] * cnt[x + d]
                res += cnt[x] * col_cnt[x - d] * cnt[x - d]
        return res


if __name__ == '__main__':
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    print(detectSquares.count([11, 10]))
    print(detectSquares.count([14, 8]))
    detectSquares.add([11, 2])
    print(detectSquares.count([11, 10]))
