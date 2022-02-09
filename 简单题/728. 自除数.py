def selfDividingNumbers(left: int, right: int) -> [int]:
    res = []
    for i in range(left, right+1):
        is_dividing_numbers = True
        tmp = []
        for j in str(i):
            t = int(j)
            if t == 0:
                is_dividing_numbers = False
                break
            if t != 1 and t not in tmp:
                if i % t != 0:
                    is_dividing_numbers = False
                    break
                tmp.append(t)
        if is_dividing_numbers:
            res.append(i)
    return res


if __name__ == '__main__':
    print(selfDividingNumbers(1, 10000))


