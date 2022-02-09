def sumOddLengthSubarrays(arr: [int]) -> int:
    n = arr.__len__()
    res = 0
    for i, a in enumerate(arr):
        res += a*((i//2+1)*((n-i+1)//2)+((i+1)//2)*((n-i)//2))
    return res


if __name__ == '__main__':
    print(sumOddLengthSubarrays([1,4,2,5,3]))
    print(sumOddLengthSubarrays([1,2]))
    print(sumOddLengthSubarrays([10,11,12]))

