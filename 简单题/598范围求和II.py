def maxCount(m: int, n: int, ops: [[int]]) -> int:
    return min(op[0] for op in ops)*min(op[1] for op in ops) if ops else m*n


if __name__ == '__main__':
    print(maxCount(m=40000, n=40000, ops=[]))