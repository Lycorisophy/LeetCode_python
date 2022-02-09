def complexNumberMultiply(num1: str, num2: str) -> str:
    n1, n2 = num1.split('+'), num2.split('+')
    n1x, n1y = n1[0], n1[1]
    n2x, n2y = n2[0], n2[1]
    n1y, n2y = n1y.rstrip('i'), n2y.rstrip('i')
    n1x, n1y, n2x, n2y = int(n1x), int(n1y), int(n2x), int(n2y)
    x = n1x * n2x - n1y * n2y
    y = n2x * n1y + n1x * n2y
    return str(x) + '+' + str(y) + 'i'


if __name__ == '__main__':
    print(complexNumberMultiply(num1="1+1i", num2="1+1i"))
    print(complexNumberMultiply(num1="1+-1i", num2="1+-1i"))
