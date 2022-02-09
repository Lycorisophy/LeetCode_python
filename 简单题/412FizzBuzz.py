def fizzBuzz(n: int) -> [str]:
    res = []
    c1, c2, c3 = 0, 0, 0
    for i in range(1, n+1):
        c1 += 1
        c2 += 1
        c3 += 1
        if c3 == 15:
            res.append('FizzBuzz')
            c1, c2, c3 = 0, 0, 0
        elif c2 == 5:
            res.append('Buzz')
            c2 = 0
        elif c1 == 3:
            res.append('Fizz')
            c1 = 0
        else:
            res.append(str(i))
    return res


if __name__ == '__main__':
    print(fizzBuzz(n=105))

