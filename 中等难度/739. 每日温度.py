# 单调栈
def dailyTemperatures(T: [int]) -> [int]:
    n = len(T)
    if n == 1:
        return [0]
    stack = [[T[0], 0]]
    res = [0] * n
    for i in range(1, n):
        t = T[i]
        while stack and stack[-1][0] < t:
            item = stack.pop()
            idx = item[1]
            res[idx] = i - idx
        stack.append((t, i))
    return res


if __name__ == '__main__':
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures([30, 40, 50, 60]))
    print(dailyTemperatures([30, 60, 90]))
