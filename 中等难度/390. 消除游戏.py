def lastRemaining(n: int) -> int:
    if n == 1:
        return 1
    return 2*(n//2+1-lastRemaining(n//2))


if __name__ == '__main__':
    print(lastRemaining(1))
    print(lastRemaining(5))
    print(lastRemaining(9))
