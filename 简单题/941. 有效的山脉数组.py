def validMountainArray(arr: [int]) -> bool:
    pre = arr[0]
    n = arr.__len__()
    if n < 3:
        return False
    has_rise = False
    has_de = False
    for i, data in enumerate(arr[1:]):
        if data > pre:
            pre = data
            has_rise = True
        elif data == pre:
            return False
        else:
            has_de = True
            pre = data
            break
    if i + 2 == n:
        if has_rise and has_de:
            return True
        return False
    for data in arr[i+2:]:
        if data < pre:
            pre = data
        else:
            return False
    if has_rise and has_de:
        return True
    return False


if __name__ == '__main__':
    print(validMountainArray([3,2,1]))
    print(validMountainArray([3,5,5]))
    print(validMountainArray([0,3,2,1]))
