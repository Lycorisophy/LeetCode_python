def integerBreak(n: int) -> int:
        for i in range(1, 9):
            t = i**2
            if t >= n:
                break
        s = n // i
        r = n % i
        if r != 0:
            return i**(s-1)*(i+r)
        else:
            return i**s


if __name__ == '__main__':
    print(integerBreak(2))
