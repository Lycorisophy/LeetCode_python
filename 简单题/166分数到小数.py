def fractionToDecimal(numerator: int, denominator: int) -> str:
    return str(numerator%denominator)


if __name__ == '__main__':
    print(fractionToDecimal(numerator=1, denominator=3))
