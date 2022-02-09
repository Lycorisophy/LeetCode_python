def hIndex(citations: [int]) -> int:
    citations.sort()
    n = citations.__len__()
    h = n
    for i, citation in enumerate(citations):
        if citation < h:
            h -= 1
        else:
            return h
    return h


if __name__ == '__main__':
    print(hIndex([3, 0, 6, 1, 5]))
    print(hIndex([0, 0, 0]))
    print(hIndex([99, 100, 88]))