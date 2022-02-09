import math
from collections import deque


def snakesAndLadders(board: [[int]]) -> int:
    def getPos(idx: int, N: int) -> (int, int):
        r, c = (idx - 1) // N, (idx - 1) % N
        if r % 2 == 1:
            c = N - 1 - c
        return N - 1 - r, c


    n = board.__len__()
    if n == 2:
        return 1
    vis = set()
    q = deque([(1, 0)])
    while q:
        idx, step = q.popleft()
        for i in range(1, 6 + 1):
            idx_nxt = idx + i
            if idx_nxt > n * n:  # 超出边界
                break
            x_nxt, y_nxt = getPos(idx_nxt, n)  # 得到下一步的行列
            if board[x_nxt][y_nxt] > 0:  # 存在蛇或梯子
                idx_nxt = board[x_nxt][y_nxt]
            if idx_nxt == n * n:  # 到达终点
                return step + 1
            if idx_nxt not in vis:
                vis.add(idx_nxt)
                q.append((idx_nxt, step + 1))  # 扩展新状态
    return -1


if __name__ == '__main__':
    print(snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))
    print(snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]]))
