def minSteps(n: int) -> int:
    if n == 1:
        return 0
    for i in range(2, max(n//2, 2)):
        if n % i == 0:
            return i+minSteps(n//i)
    return n


if __name__ == '__main__':
    print(minSteps(10))
    print(minSteps(15))
    print(minSteps(20))
