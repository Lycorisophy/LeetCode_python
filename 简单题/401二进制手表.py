def readBinaryWatch(num: int) -> [str]:
    s = [0,1,2,3,4,5,6,7,8,9]
    tmp = list(combinations(iterable=s, r=num))
    res = [[0,0,0,0,0,0,0,0,0,0]] * len(tmp)
    for i in range(len(tmp)):
        for j in range(num):
            res[i][tmp[i][j]] = 1
    return res

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(iterable)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(iterable)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)

if __name__ == '__main__':
    print(readBinaryWatch(num = 3))