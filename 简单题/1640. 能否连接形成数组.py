def canFormArray(arr: [int], pieces: [[int]]) -> bool:
    dic = {}
    for piece in pieces:
        dic[piece[0]] = piece
    res = []
    for a in arr:
        tmp = dic.get(a)
        if tmp:
            res += tmp
    return arr == res


if __name__ == '__main__':
    print(canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))
    print(canFormArray([91,4,64,78], pieces = [[78],[4,64],[91]]))
    print(canFormArray(arr = [1,3,5,7], pieces = [[2,4,6,8]]))
