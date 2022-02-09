def multiply(num1: str, num2: str) -> str:
    num_list = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    num1, num2 = num1[::-1], num2[::-1]
    res = 0
    for i, n1 in enumerate(num1):
        n1 = num_list[n1]
        for j, n2 in enumerate(num2):
            n2 = num_list[n2]
            res += (n1*10**i)*(n2*10**j)
    return str(res)


if __name__ == '__main__':
    print(multiply(num1="123", num2="456"))
    print(multiply(num1="2", num2="3"))
