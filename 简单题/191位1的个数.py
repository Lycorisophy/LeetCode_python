def hammingWeight(n: int) -> int:
    n = bin(n)
    num = 0
    for data in n:
        if data == '1':
            num += 1
    return num


if __name__ == "__main__":
    print(hammingWeight(n=65))