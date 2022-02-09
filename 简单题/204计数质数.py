def countPrimes(n: int) -> int:
    if n == 0 or n == 1 or n == 2:
        return 0
    count = 0
    isPrimes = [True] * (n+1)
    for j in range(2, n):
        if isPrimes[j]:
            m = 2
            while j * m <= n:
                isPrimes[j * m] = False
                m += 1
    for k in range(2, n):
        if isPrimes[k]:
            count += 1
    return count


if __name__ == '__main__':
    print(countPrimes(1000))
