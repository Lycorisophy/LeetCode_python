import random


def rand7():
    return random.randint(1, 7)


def rand10():
    res = [[0 for _ in range(7)] for _ in range(7)]
    x, y = 0, -1
    for i in range(4):
        for j in range(1, 11):
            y += 1
            if y == 7:
                y = 0
                x += 1
            res[x][y] = j
    while True:
        a = res[rand7() - 1][rand7() - 1]
        if a != 0:
            return a


if __name__ == '__main__':
    d = {}
    for _ in range(10000):
        a = rand10()
        if a not in d:
            d[a] = 1
        else:
            d[a] += 1
    print(d)
