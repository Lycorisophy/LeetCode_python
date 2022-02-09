from collections import deque


def openLock(deadends: [str], target: str) -> int:
    D = set(deadends)
    if '0000' in D:
        return -1
    if '0000' == target:
        return 0

    def num_prev(x: str) -> str:
        return "9" if x == "0" else str(int(x) - 1)

    def num_succ(x: str) -> str:
        return "0" if x == "9" else str(int(x) + 1)

    def get(status: str) -> [str, None, None]:
        s = list(status)
        for i in range(4):
            num = s[i]
            s[i] = num_prev(num)
            yield "".join(s)
            s[i] = num_succ(num)
            yield "".join(s)
            s[i] = num

    Q = deque([('0000', 0)])
    seen = {"0000"}
    while Q:
        status, step = Q.popleft()
        for nxt in get(status):
            if nxt not in D and nxt not in seen:
                if nxt == target:
                    return step + 1
                Q.append((nxt, step+1))
                seen.add(nxt)
    return -1


if __name__ == '__main__':
    print(openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
    print(openLock(deadends=["8888"], target="0009"))
    print(openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888"))
    print(openLock(['0000'], '8888'))
