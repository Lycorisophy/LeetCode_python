def checkPerfectNumber(num: int) -> bool:
    return num in [6, 28, 496, 8128, 33550336]




if __name__ == '__main__':
    print(checkPerfectNumber(28))
    print(checkPerfectNumber(6))
    print(checkPerfectNumber(496))
    print(checkPerfectNumber(8128))
    print(checkPerfectNumber(2))
    print(checkPerfectNumber(1))
