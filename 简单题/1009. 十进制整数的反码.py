def bitwiseComplement(N: int) -> int:
    if N < 32:
        M = [2, 4, 8, 16, 32]
    elif N < 1024:
        M = [64, 128, 256, 512, 1024]
    elif N < 32768:
        M = [2048, 4096, 8192, 16384, 32768]
    elif N < 1048576:
        M = [65536, 131072, 262144, 524288, 1048576]
    elif N < 33554432:
        M = [2097152, 4194304, 8388608, 16777216, 33554432]
    else:
        M = [67108864, 134217728, 268435456, 536870912, 1073741824]
    for m in M:
        if m > N:
            return m - N - 1


if __name__ == '__main__':
    print(bitwiseComplement(5))
    print(bitwiseComplement(7))
    print(bitwiseComplement(10))
