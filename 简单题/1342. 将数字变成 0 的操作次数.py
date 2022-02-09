def numberOfSteps(num: int) -> int:
    num = bin(num)[2:]
    return num.__len__()-1+num.count('1')


if __name__ == '__main__':
    print(numberOfSteps(14))
    print(numberOfSteps(8))
    print(numberOfSteps(123))
