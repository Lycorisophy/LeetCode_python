def findJudge(N: int, trust: [[int]]) -> int:
    A = set()
    B = {i: 0 for i in range(1, N + 1)}
    C = set(i for i in range(1, N + 1))
    for a, b in trust:
        A.add(a)
        B[b] += 1
    J = C - A
    if J.__len__() != 1:
        return -1
    j = J.pop()
    if B[j] != N-1:
        return -1
    return j


if __name__ == '__main__':
    print(findJudge(N=2, trust=[[1, 2]]))
    print(findJudge(N=3, trust=[[1, 3], [2, 3]]))
    print(findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))
    print(findJudge(N=3, trust=[[1, 2], [2, 3]]))
    print(findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
