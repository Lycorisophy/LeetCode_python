def superPow(a: int, b: [int]) -> int:
    def myPow(x: int, y: int, z: int) -> int:
        x %= z
        res = 1
        for _ in range(y):
            res *= x
            res %= base
        return res
    if not b:
        return 1
    base = 1337
    last = b.pop(-1)
    return (myPow(a, last, base) * myPow(superPow(a, b), 10, base)) % base


if __name__ == '__main__':
    print(superPow(a=2147483647, b=[2, 0, 0]))
