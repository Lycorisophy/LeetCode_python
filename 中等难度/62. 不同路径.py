def uniquePaths(m: int, n: int) -> int:
    def num(n):
        if n == 0:
            return 1
        return n * num(n - 1)

    m -= 1
    n -= 1
    c = m + n
    return num(c)//num(m)//num(n)


if __name__ == '__main__':
    print(uniquePaths(m = 3, n = 7))
    print(uniquePaths(3,2))
    print(uniquePaths(7,3))
