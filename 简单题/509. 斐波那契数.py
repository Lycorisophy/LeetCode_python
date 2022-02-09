def fib(n: int) -> int:
    if n <= 30:
        fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
                10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
        return fibs[n]
    else:
        return fib(n-2)+fib(n-1)


if __name__ == '__main__':
    n = int(input('请输入斐波那契项数n'))
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[i-1]+fibs[i-2])
    for fib in fibs:
        print('{}'.format(fib), end=',')
