def findComplement(num: int) -> int:
    for i, d in enumerate(bin(num)[2:][::-1]):
        if d == '1':
            m = i
    return 2**(m+1)-num-1


if __name__ == '__main__':
    print(findComplement(1))
