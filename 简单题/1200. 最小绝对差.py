def minimumAbsDifference(arr: [int]) -> [[int]]:
    arr.sort()
    res = {}
    for i in range(1, arr.__len__()):
        x, y = arr[i-1:i+1]
        dis = y - x
        if res.get(dis) is None:
            res[dis] = [[x, y]]
        else:
            res[dis].append([x, y])
    return res[min(res.keys())]


if __name__ == '__main__':
    print(minimumAbsDifference([4,2,1,3]))
    print(minimumAbsDifference([1,3,6,10,15]))
    print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
